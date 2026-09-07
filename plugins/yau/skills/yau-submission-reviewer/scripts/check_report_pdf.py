#!/usr/bin/env python3
"""丘奖研究报告 PDF 形式检查（确定性部分）。

只做能机械判定的事：文件是不是 PDF、页数、sha256、封页五字段是否出现、
官方规定的章节顺序（题目→作者→摘要→关键词→目录→正文→参考文献→致谢）能否在文本中依次找到。
判断不了的（内容质量、分工是否具体、有偿与否是否写清）留给 skill 主流程人工核对。

用法：
    python3 check_report_pdf.py <report.pdf> [--plag <查重版.pdf>] [--json]

--plag 给出查重时提交的那份 PDF，脚本比较两者 sha256，判定"查重版 = 提交版"。
退出码：0 = 全部形式项通过；1 = 有 revise/blocked 项；2 = 无法读取。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

COVER_FIELDS = {
    "姓名": [r"姓\s*名", r"作者", r"\bName\b", r"\bAuthor"],
    "省份/州": [r"省", r"州", r"\bProvince\b", r"\bState\b"],
    "国别": [r"国\s*别", r"国家", r"中国", r"\bCountry\b", r"\bChina\b"],
    "指导老师": [r"指导(老师|教师)", r"导师", r"\bAdvisor\b", r"\bMentor\b", r"\bSupervisor\b"],
    "报告标题": [r"题\s*目", r"标\s*题", r"\bTitle\b"],
}

# 官方顺序：第二页起依次为 题目、作者、摘要、关键词、目录、正文；参考文献另起一页；致谢页存在
SECTION_ORDER = [
    ("摘要", [r"摘\s*要", r"\bAbstract\b"]),
    ("关键词", [r"关键词", r"关键字", r"\bKey\s*words?\b"]),
    ("目录", [r"目\s*录", r"\bContents?\b", r"\bTable of Contents\b"]),
    ("参考文献", [r"参考文献", r"\bReferences?\b", r"\bBibliography\b"]),
    ("致谢", [r"致\s*谢", r"\bAcknowledg(e)?ments?\b"]),
]

ACK_ELEMENTS = {
    "分工/贡献": [r"分工", r"贡献", r"负责", r"\bcontribut"],
    "导师有偿/无偿": [r"有偿", r"无偿", r"报酬", r"\bpaid\b", r"\bunpaid\b", r"费用"],
    "AI 披露": [r"\bAI\b", r"人工智能", r"ChatGPT", r"GPT", r"Claude", r"Gemini", r"DeepSeek", r"大模型", r"\bLLM\b"],
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            return f.read(5) == b"%PDF-"
    except OSError:
        return False


def page_texts(path: Path) -> list[str]:
    """优先 pdftotext（保留版面），退回 pypdf。返回每页文本。"""
    try:
        out = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True, text=True, check=True, timeout=120,
        ).stdout
        pages = out.split("\f")
        if pages and not pages[-1].strip():
            pages = pages[:-1]
        if any(p.strip() for p in pages):
            return pages
    except (OSError, subprocess.SubprocessError):
        pass
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        return [(p.extract_text() or "") for p in reader.pages]
    except Exception:  # noqa: BLE001
        return []


def any_match(patterns: list[str], text: str) -> bool:
    return any(re.search(p, text, flags=re.IGNORECASE) for p in patterns)


def check(report: Path, plag: Path | None) -> dict:
    result: dict = {"file": str(report), "items": [], "status": "pass"}

    def add(name: str, status: str, evidence: str, level: str = "form"):
        result["items"].append({"item": name, "status": status, "evidence": evidence, "level": level})

    if not report.exists() or not is_pdf(report):
        add("文件格式为 PDF", "blocked", "不是 PDF 文件或文件不存在", "disqualify")
        result["status"] = "blocked"
        return result
    add("文件格式为 PDF", "pass", "PDF 头校验通过")

    digest = sha256(report)
    result["sha256"] = digest
    pages = page_texts(report)
    result["pages"] = len(pages)
    if not pages or not any(p.strip() for p in pages):
        add("PDF 含可提取文本", "revise", "未提取到文本——可能是扫描图片版；官方要求电子版 PDF，且查重系统无法处理图片")
        result["status"] = "revise"
        return result
    add("PDF 含可提取文本", "pass", f"{len(pages)} 页，文本可提取")

    cover = "\n".join(pages[:2])
    missing = [k for k, pats in COVER_FIELDS.items() if not any_match(pats, cover)]
    if missing:
        add("封页五字段", "revise", f"前两页未识别到：{'、'.join(missing)}（识别基于关键词，请人工复核）")
    else:
        add("封页五字段", "pass", "姓名/省份州/国别/指导老师/标题 均在前两页出现")

    full = "\n".join(pages)
    positions = {}
    for name, pats in SECTION_ORDER:
        m = None
        for p in pats:
            m = re.search(p, full, flags=re.IGNORECASE)
            if m:
                break
        positions[name] = m.start() if m else None
    absent = [n for n, pos in positions.items() if pos is None]
    if absent:
        add("官方章节齐全", "revise", f"未找到：{'、'.join(absent)}")
    else:
        add("官方章节齐全", "pass", "摘要/关键词/目录/参考文献/致谢 均存在")
    present = [(n, pos) for n, pos in positions.items() if pos is not None]
    ordered = [n for n, _ in sorted(present, key=lambda x: x[1])]
    expected = [n for n, _ in SECTION_ORDER if n in ordered]
    if ordered != expected:
        add("章节顺序符合官方顺序", "revise", f"实际出现顺序：{' → '.join(ordered)}；官方顺序：{' → '.join(expected)}")
    else:
        add("章节顺序符合官方顺序", "pass", " → ".join(ordered))

    ack_pos = positions.get("致谢")
    if ack_pos is not None:
        ack_text = full[ack_pos: ack_pos + 6000]
        lacking = [k for k, pats in ACK_ELEMENTS.items() if not any_match(pats, ack_text)]
        if lacking:
            add("致谢页三要件关键词", "revise",
                f"致谢页附近未见：{'、'.join(lacking)}（关键词初筛；无 AI 使用也须在致谢页写明'未使用'）", "disqualify")
        else:
            add("致谢页三要件关键词", "pass", "分工/有偿无偿/AI 三类关键词均出现，内容是否具体需人工核对", "disqualify")

    if plag is not None:
        if not plag.exists():
            add("查重版 = 提交版", "revise", f"查重版文件不存在：{plag}", "disqualify")
        else:
            pd = sha256(plag)
            if pd == digest:
                add("查重版 = 提交版", "pass", f"sha256 一致 {digest[:12]}…", "disqualify")
            else:
                add("查重版 = 提交版", "blocked",
                    f"sha256 不一致（提交版 {digest[:12]}… / 查重版 {pd[:12]}…）——须用最终版重新出具查重报告", "disqualify")

    statuses = [i["status"] for i in result["items"]]
    if "blocked" in statuses:
        result["status"] = "blocked"
    elif "revise" in statuses:
        result["status"] = "revise"
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", type=Path)
    ap.add_argument("--plag", type=Path, default=None, help="查重时使用的 PDF，用于核对是否同一版本")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    res = check(args.report, args.plag)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"文件：{res['file']}")
        if "pages" in res:
            print(f"页数：{res['pages']}   sha256：{res.get('sha256', '')}")
        for it in res["items"]:
            mark = {"pass": "✅", "revise": "⚠️", "blocked": "⛔"}[it["status"]]
            star = " ★" if it["level"] == "disqualify" else ""
            print(f"{mark} {it['item']}{star}：{it['evidence']}")
        print(f"总判定：{res['status']}")
    if res["status"] == "pass":
        return 0
    if "pages" not in res:
        return 2
    return 1


if __name__ == "__main__":
    sys.exit(main())
