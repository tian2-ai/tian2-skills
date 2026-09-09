#!/usr/bin/env python3
"""Render a yau-family markdown report into Tian2-branded HTML / PDF / DOCX.

Usage:
    python3 render_report.py report.md [--formats html,pdf,docx] [--out DIR]

Part of the yau skill family's unified deliverable pipeline
(assets/report-style/README.md). Brand: Tian2 — cream/ink editorial,
coral reserved for blocked/★. Assets are located relative to this script,
so the skill folder can live anywhere.

Dependencies (fail loudly, never degrade silently):
    html : pandoc                     (brew install pandoc)
    pdf  : pandoc + xelatex + xeCJK   (brew install pandoc; brew install --cask mactex-no-gui)
    docx : pandoc + reference.docx    (shipped alongside this script)
"""

import argparse
import datetime
import html as html_mod
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
STYLE_DIR = SCRIPT_DIR.parent / "assets" / "report-style"
CSS_FILE = STYLE_DIR / "tian2-report.css"
LATEX_TEMPLATE = STYLE_DIR / "tian2-report.latex"
REFERENCE_DOCX = STYLE_DIR / "reference.docx"

HEADER_LABEL = "TIAN2 · YAU SCIENCE AWARDS"

# Emoji: pictographs, symbols, flags, and the variation selector / ZWJ glue.
EMOJI_RE = re.compile(
    "["
    "\U0001F000-\U0001FAFF"   # pictographs, incl. 🤖
    "\U00002700-\U000027BF"   # dingbats
    "\U0001F1E6-\U0001F1FF"   # flags
    "\U00002B00-\U00002BFF"   # arrows/stars block (⬛ ⭐) — ★ U+2605 unaffected
    "\U0000FE0F\U0000200D"    # variation selector-16, ZWJ
    "]+"
)


def die(msg: str) -> None:
    sys.exit(f"render_report: ERROR: {msg}")


def check_dependencies(formats: list[str]) -> None:
    problems = []
    if shutil.which("pandoc") is None:
        problems.append("pandoc 未安装 — install: brew install pandoc")
    if "pdf" in formats and shutil.which("xelatex") is None:
        problems.append(
            "xelatex 未安装（PDF 需要）— install: brew install --cask mactex-no-gui "
            "（或 basictex + tlmgr install xecjk titlesec framed fvextra colortbl booktabs etoolbox fancyhdr）"
        )
    if "pdf" in formats and not LATEX_TEMPLATE.is_file():
        problems.append(f"LaTeX 模板缺失: {LATEX_TEMPLATE}")
    if "html" in formats and not CSS_FILE.is_file():
        problems.append(f"CSS 缺失: {CSS_FILE}")
    if "docx" in formats and not REFERENCE_DOCX.is_file():
        problems.append(f"reference.docx 缺失: {REFERENCE_DOCX}（见 assets/report-style/README.md 重新生成）")
    if problems:
        die("依赖不满足，不做静默降级：\n  - " + "\n  - ".join(problems))


def strip_emoji(text: str) -> str:
    """PDF/docx: Tian2 rules forbid emoji. 🤖 → [AI]; the rest are dropped."""
    text = text.replace("\U0001F916", "[AI]")  # 🤖
    return EMOJI_RE.sub("", text)


def _display_len(cell: str) -> int:
    """Approximate display width: CJK and fullwidth chars count double."""
    return sum(2 if ord(ch) > 0x2E7F else 1 for ch in cell)


def widen_table_delimiters(md_text: str) -> str:
    """Rewrite pipe-table delimiter rows so column widths are proportional to
    column content. Pandoc reads dash counts as relative widths, which keeps
    the 7-column verdict tables readable (evidence/action columns get room)
    in PDF, docx and HTML alike."""
    lines = md_text.splitlines()
    out = list(lines)
    i = 0
    delim_re = re.compile(r"^\|(\s*:?-{2,}:?\s*\|)+\s*$")
    while i < len(lines) - 1:
        if lines[i].lstrip().startswith("|") and delim_re.match(lines[i + 1].strip()):
            header = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            ncols = len(header)
            body_start = i + 2
            j = body_start
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            weights = [max(_display_len(h), 3) for h in header]
            for row_line in lines[body_start:j]:
                cells = [c.strip() for c in row_line.strip().strip("|").split("|")]
                for k in range(min(ncols, len(cells))):
                    weights[k] = max(weights[k], _display_len(cells[k]))
            # cap so one runaway column can't starve the rest
            cap = max(6, int(sum(weights) * 0.34))
            weights = [min(w, cap) for w in weights]
            total = sum(weights) or 1
            dashes = [max(3, round(w / total * 120)) for w in weights]
            out[i + 1] = "|" + "|".join("-" * d for d in dashes) + "|"
            i = j
        else:
            i += 1
    return "\n".join(out) + ("\n" if md_text.endswith("\n") else "")


BRAND_FONTS = ("Inter", "Playfair Display", "Noto Sans SC", "Noto Serif SC")


def warn_missing_fonts() -> None:
    """PDF route: warn (loudly, on stderr) which brand fonts are absent and
    that the template falls back to system fonts. Needs fc-list; if it is not
    available the LaTeX template still falls back safely on its own."""
    fc = shutil.which("fc-list")
    if fc is None:
        return
    try:
        installed = subprocess.run([fc, ":", "family"], capture_output=True,
                                   text=True, timeout=30).stdout
    except Exception:
        return
    families = set()
    for line in installed.splitlines():
        families.update(fam.strip() for fam in line.split(","))
    missing = [f for f in BRAND_FONTS if f not in families]
    if missing:
        print(
            "  警告: 品牌字体未安装: " + ", ".join(missing)
            + " — PDF 使用系统回退（Georgia / Helvetica Neue / Songti SC / PingFang SC）。"
            + " HTML 不受影响（Google Fonts 在线加载）。",
            file=sys.stderr,
        )


def extract_title(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "审查报告"


def run_pandoc(args: list[str]) -> None:
    proc = subprocess.run(["pandoc", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        die(f"pandoc 失败 (exit {proc.returncode}):\n{proc.stderr.strip()[-3000:]}")


VERDICT_STRONG_RE = re.compile(r"<strong>(pass|revise|blocked)</strong>")
VERDICT_TD_RE = re.compile(r"(<td[^>]*>)(pass|revise|blocked)\b")


def badge(word: str) -> str:
    return f'<span class="verdict verdict--{word}">{word}</span>'


def render_html(md_file: Path, out_file: Path, title: str) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        frag = Path(tmp) / "body.html"
        run_pandoc([
            str(md_file), "-f", "markdown+east_asian_line_breaks",
            "-t", "html5", "-o", str(frag), "--wrap=none",
        ])
        body = frag.read_text(encoding="utf-8")

    # pass/revise/blocked → brand badges (coral only for blocked)
    body = VERDICT_STRONG_RE.sub(lambda m: badge(m.group(1)), body)
    body = VERDICT_TD_RE.sub(lambda m: m.group(1) + badge(m.group(2)), body)
    # wide verdict tables scroll inside their own container
    body = body.replace("<table>", '<div class="table-scroll"><table>')
    body = body.replace("</table>", "</table></div>")

    css = CSS_FILE.read_text(encoding="utf-8")
    page = (
        "<!doctype html>\n"
        '<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{html_mod.escape(title)}</title>\n"
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        f"<style>\n{css}\n</style>\n</head>\n<body>\n"
        f'<main class="report">\n{body}\n</main>\n</body>\n</html>\n'
    )
    out_file.write_text(page, encoding="utf-8")


def render_pdf(md_file: Path, out_file: Path, title: str) -> None:
    today = datetime.date.today().isoformat()
    proc = subprocess.run(
        [
            "pandoc", str(md_file), "-f", "markdown+east_asian_line_breaks",
            "-o", str(out_file), "--pdf-engine=xelatex",
            "--template", str(LATEX_TEMPLATE),
            "-M", f"title={title}",
            "-V", f"header-label={HEADER_LABEL}",
            "-V", f"date={today}",
        ],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        die(f"PDF 渲染失败 (xelatex, exit {proc.returncode}):\n{proc.stderr.strip()[-3000:]}")
    for line in (proc.stderr or "").splitlines():
        if "TIAN2-FONT-FALLBACK" in line:
            print(f"  警告: {line.strip()}", file=sys.stderr)


def render_docx(md_file: Path, out_file: Path) -> None:
    run_pandoc([
        str(md_file), "-f", "markdown+east_asian_line_breaks",
        "-o", str(out_file), "--reference-doc", str(REFERENCE_DOCX),
    ])


def main() -> None:
    ap = argparse.ArgumentParser(description="Render a markdown report to Tian2-branded HTML/PDF/DOCX.")
    ap.add_argument("report", help="markdown 报告文件")
    ap.add_argument("--formats", default="html,pdf,docx", help="逗号分隔: html,pdf,docx（默认全部）")
    ap.add_argument("--out", default=None, help="输出目录（默认与输入文件同目录）")
    args = ap.parse_args()

    src = Path(args.report).resolve()
    if not src.is_file():
        die(f"找不到输入文件: {src}")
    formats = [f.strip().lower() for f in args.formats.split(",") if f.strip()]
    unknown = [f for f in formats if f not in ("html", "pdf", "docx")]
    if unknown:
        die(f"不认识的格式: {', '.join(unknown)}（可选 html,pdf,docx）")
    check_dependencies(formats)

    out_dir = Path(args.out).resolve() if args.out else src.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    md_text = src.read_text(encoding="utf-8")
    title = extract_title(md_text)
    stem = src.stem
    # proportional column widths for wide verdict tables (all formats)
    md_sized = widen_table_delimiters(md_text)

    produced = []
    with tempfile.TemporaryDirectory() as tmp:
        html_md = Path(tmp) / f"{stem}.html.md"
        html_md.write_text(md_sized, encoding="utf-8")
        # PDF/docx use an emoji-free copy (🤖 → [AI]); HTML keeps emoji as-is.
        clean_md = Path(tmp) / f"{stem}.noemoji.md"
        clean_md.write_text(strip_emoji(md_sized), encoding="utf-8")

        if "html" in formats:
            out = out_dir / f"{stem}.html"
            render_html(html_md, out, title)
            produced.append(out)
        if "pdf" in formats:
            warn_missing_fonts()
            out = out_dir / f"{stem}.pdf"
            render_pdf(clean_md, out, title)
            produced.append(out)
        if "docx" in formats:
            out = out_dir / f"{stem}.docx"
            render_docx(clean_md, out)
            produced.append(out)

    for p in produced:
        print(f"  ✓ {p}  ({p.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
