<div align="center">

# 📚 PaperGrab

### 学生专用 PDF 转 Word 工具 — 批量转换课件 · 保留格式 · 命令行操作

A PDF-to-Word converter designed for students: batch-convert courseware and papers to editable Word, with format preservation.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-green.svg)](https://github.com/12341141552204/pdf2word)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/12341141552204/pdf2word)](https://github.com/12341141552204/pdf2word)

</div>

## 🎯 为什么学生需要这个工具

老师发的课件是 PDF，想改笔记要手动重新打字。论文 PDF 想引用内容，复制粘贴排版全乱。

**PaperGrab 帮你：**
- 📄 PDF 课件一键转 Word，直接在 Word 里做笔记
- 📑 论文转 Word，保留段落格式方便引用编辑
- 📦 整个文件夹的 PDF 批量转换，期末复习效率翻倍

## ✨ 功能特性

| 功能 | 说明 |
|---|---|
| 批量转换 | 一次转换文件夹内所有 PDF |
| 保留格式 | 段落、表格、列表格式完整保留 |
| 单文件转换 | 指定单个 PDF 精准转换 |
| PDF 信息 | 查看页数、文件大小、是否加密 |
| 保留图片 | PDF 中的图片自动提取到 Word |

## 📦 安装

```bash
# 克隆仓库
git clone https://github.com/12341141552204/pdf2word.git

# 安装依赖
pip install -r requirements.txt
```

## 🚀 使用方法

### 1. 转换单个 PDF（课件/论文）

```bash
# 转换老师的课件
python main.py convert "D:\课件\高等数学第3章.pdf"

# 指定输出路径
python main.py convert "D:\课件\高等数学第3章.pdf" -o "D:\笔记\高数第3章.docx"
```

### 2. 批量转换（期末复习）

```bash
# 转换整个课件文件夹
python main.py batch "D:\本学期课件\"
```

转换效果：
```
输入：
  高等数学第1章.pdf
  高等数学第2章.pdf
  英语阅读材料.pdf
  毛概课件.pdf

输出：
  高等数学第1章.docx
  高等数学第2章.docx
  英语阅读材料.docx
  毛概课件.docx
```

### 3. 查看 PDF 信息

```bash
python main.py info "D:\论文\xxx大学学位论文.pdf"
```

## 📖 命令参考

| 命令 | 用途 |
|---|---|
| `convert <PDF>` | 转换单个 PDF |
| `convert <PDF> -o <输出>` | 指定输出路径 |
| `batch <文件夹>` | 批量转换 |
| `batch <文件夹> --recursive` | 递归扫描子目录 |
| `info <PDF>` | 查看 PDF 页数和信息 |

## 💡 使用场景

| 场景 | 操作 |
|---|---|
| 老师发 PDF 课件，想做笔记 | `convert` 转成 Word，直接在里面写笔记 |
| 下载论文 PDF，要引用内容 | `convert` 转成 Word，复制粘贴排版不乱 |
| 期末复习，几十个 PDF 课件 | `batch` 批量转换，一次性搞定 |
| 毕业论文 PDF 查重前 | `info` 查看页数，确认格式 |

## 🤝 贡献

欢迎提交 Issue 和 PR！请阅读 [贡献指南](CONTRIBUTING.md)。

## 💖 赞助

如果这个工具帮你省了整理笔记的时间，请考虑赞助：

| 方案 | 月费 | 权益 |
|---|---|---|
| 🥤 随手一杯 | ¥5 | README 署名 + 月度进展 |
| 🚀 催更选手 | ¥15 | 提前体验 + 优先排功能 |
| 👑 金主爸爸 | ¥50 | 功能优先建议 + 项目挂名 |

👉 [爱发电赞助](https://afdian.com/a/JingJingZ)

## 📄 许可证

[MIT License](LICENSE) - 自由使用，欢迎商用
