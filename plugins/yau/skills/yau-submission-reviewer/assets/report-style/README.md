# Tian2 Report Style — yau skill 家族统一产出规范

yau-* 系列 skill 的**书面交付物**（材料审查报告、研究计划、答辩讲义、AI 披露自查表等）
统一用这一套资产渲染成 tian2-design 品牌的三格式：HTML（在线阅读）、PDF（打印/存档）、
DOCX（学校经办人续改）。写完 markdown 之后一条命令出全部格式，不要为单个 skill
另起炉灶写样式。

## 用法

```bash
python3 scripts/render_report.py review-report.md                     # 三格式，输出到 md 同目录
python3 scripts/render_report.py review-report.md --formats html,pdf  # 只要其中几种
python3 scripts/render_report.py review-report.md --out /tmp/out      # 指定输出目录
```

脚本按自身位置定位这些资产（相对路径），skill 目录放在哪台机器都能跑。

## 这套资产是什么

| 文件 | 作用 |
|---|---|
| `tian2-report.css` | HTML 完整品牌样式：奶油 `#F5EDDC` 底、墨色 `#2C2416` 字与线、珊瑚 `#E8614C` **只用于 blocked/★**；pass/revise/blocked 三色徽章（薄荷/芥黄/珊瑚）；判定表横向滚动不挤压；`@media print` 打印友好 |
| `tian2-report.latex` | pandoc + XeLaTeX 模板：xeCJK 中文、奶油页底、页眉细墨线 + TIAN2 眉标、页脚页码、衬线标题（Playfair/Noto Serif SC 回退 Georgia/Songti SC）、longtable 缩字号防溢出 |
| `reference.docx` | pandoc `--reference-doc` 样式参考：标题层次/正文/表格对齐品牌 |

## 品牌规则（渲染层负责执行）

- 奶油底、墨色字、2.5px 墨线；无阴影、无渐变、无 emoji。
- **珊瑚色只给 blocked/★**（取消资格级）；pass 用薄荷 `#8FB89A`，revise 用芥黄 `#D9A441`。
- PDF/DOCX 渲染前 emoji 一律处理：`🤖` → `[AI]`，其余删除。HTML 保留原文。
- 宽表（7 列判定表）按列内容自动分配列宽；PDF 里长表缩到 footnotesize，允许跨页。

## 字体策略

| 格式 | 英文 | 中文 | 说明 |
|---|---|---|---|
| HTML | Playfair Display / Inter / Bebas Neue（Google Fonts 在线） | Noto Serif SC / Noto Sans SC | 离线时回退 Georgia / Helvetica Neue / Songti SC / PingFang SC，样式栈里已写好 |
| PDF | Inter → Helvetica Neue → Arial；标题 Playfair Display → Georgia | Noto Sans SC → PingFang SC；标题 Noto Serif SC → Songti SC | 模板里 `\IfFontExistsTF` 逐级回退；缺品牌字体时 render_report.py 会在 stderr 打警告 |
| DOCX | Georgia（标题）/ Arial（正文） | Songti SC（标题）/ PingFang SC（正文） | **刻意用系统常见字体**做回退，保证收件人（学校 Windows/Mac）打开不跑版；Word 里没有 Playfair/Inter |

想让 PDF 用足品牌字体：本机安装 Playfair Display、Inter、Noto Serif SC、Noto Sans SC
（Google Fonts 免费下载），模板会自动优先选用。

## 依赖清单

| 依赖 | 用于 | 安装 |
|---|---|---|
| pandoc ≥ 3 | 三格式都要 | `brew install pandoc` |
| XeLaTeX（TeX Live，含 xeCJK/titlesec/framed/fvextra/colortbl/booktabs/fancyhdr/etoolbox） | PDF | `brew install --cask mactex-no-gui` |
| fontconfig（`fc-list`，可选） | 缺字体警告 | `brew install fontconfig` |
| python-docx（可选） | 只在校验 docx 时用，渲染不需要 | `pip3 install python-docx` |

依赖缺失时脚本直接报错并给出安装命令，**不静默降级**。

（PDF 备选路线 weasyprint 未采用：本机未安装，且 pandoc+xelatex 对 xeCJK 中文与
longtable 跨页的控制更成熟。）

## 其他 yau-* skill 怎么接入

1. 交付物先写成 markdown（标题用 `#`/`##`，判定表用 pipe table，判定词只写
   `pass` / `revise` / `blocked`，HTML 会自动变徽章）。
2. 调本 skill 的脚本渲染（从任何 yau-* skill 里都可以指过来）：
   `python3 <yau-submission-reviewer>/scripts/render_report.py <你的.md> --out <目录>`。
3. 页眉眉标默认 `TIAN2 · YAU SCIENCE AWARDS`，家族通用，不必改。

## 重新生成 reference.docx

reference.docx 由 pandoc 默认参考文档改字体/颜色而来。如需重做：
`pandoc --print-default-data-file reference.docx > ref.docx`，再用 python-docx 把
Normal/Heading1-9/Title/Table 等样式的西文字体设为 Georgia/Arial、中文（`w:eastAsia`）
设为 Songti SC/PingFang SC、颜色设为墨色 `2C2416`。
