<div align="center">

# 📄 PDF to Word Converter

### PDF 转 Word，一键搞定 — 批量转换 · 保留格式 · 命令行工具

A Python tool to batch convert PDF files to editable Word documents on Windows.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-green.svg)](https://github.com/12341141552204/pdf2word)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/12341141552204/pdf2word?style=social)](https://github.com/12341141552204/pdf2word)

</div>

---

## ✨ 功能特性

| 功能 | 说明 |
|---|---|
| 📄 **单文件转换** | 将单个 PDF 转换为可编辑的 Word 文档 |
| 📁 **批量转换** | 一键转换文件夹内所有 PDF 文件 |
| 🎨 **保留格式** | 自动保留原 PDF 的排版、表格、图片和文字格式 |
| 📑 **指定页码** | 支持只转换指定页码范围（如第 3-10 页） |
| ℹ️ **文件信息** | 查看 PDF 页数等基本信息 |
| 🚀 **简单易用** | 一行命令完成转换，无需复杂操作 |

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/12341141552204/pdf2word.git
cd pdf2word
pip install -r requirements.txt
```

### 单文件转换

```bash
# 基本用法：生成同名 .docx 文件
python main.py convert "C:\Documents\report.pdf"

# 指定输出文件名
python main.py convert "report.pdf" -o "my_report.docx"

# 只转换第 3-10 页（从 0 开始计数）
python main.py convert "report.pdf" --start 2 --end 10
```

### 批量转换

```bash
# 转换文件夹内所有 PDF
python main.py batch "C:\Documents"

# 输出到指定文件夹
python main.py batch "C:\Documents" -o "C:\Output"
```

转换过程示例：
```
Found 3 PDF file(s)

[1/3] Converting: report_2024.pdf -> report_2024.docx
  Done! Saved to: C:\Output\report_2024.docx
[2/3] Converting: contract.pdf -> contract.docx
  Done! Saved to: C:\Output\contract.docx
[3/3] Converting: invoice.pdf -> invoice.docx
  Done! Saved to: C:\Output\invoice.docx

Results: 3 succeeded, 0 failed, 3 total.
```

### 查看 PDF 信息

```bash
python main.py info "C:\Documents\report.pdf"
# 输出:
# File: report.pdf
# Pages: 24
```

## 📖 命令参考

| 命令 | 说明 | 示例 |
|---|---|---|
| `convert` | 转换单个 PDF | `python main.py convert "file.pdf" [-o output.docx] [--start N] [--end M]` |
| `batch` | 批量转换文件夹 | `python main.py batch "folder" [-o output_folder] [--start N] [--end M]` |
| `info` | 查看 PDF 信息 | `python main.py info "file.pdf"` |

## 🛠️ 技术栈

- **Python 3.8+**
- [pdf2docx](https://github.com/dothinking/pdf2docx) - PDF 转 Word 核心引擎
- 纯命令行界面，无需 GUI

## 📋 使用场景

| 场景 | 说明 |
|---|---|
| 办公文档 | PDF 报告转 Word 修改编辑 |
| 合同处理 | 批量转换合同 PDF 为 Word 格式 |
| 学习资料 | 课件、论文 PDF 转 Word 做笔记 |
| 发票管理 | 批量转换发票 PDF 为 Word 归档 |

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建分支 `git checkout -b feature/YourFeature`
3. 提交更改 `git commit -m 'Add some feature'`
4. 推送分支 `git push origin feature/YourFeature`
5. 发起 Pull Request

## 💖 支持这个项目

如果这个工具对你有帮助，请考虑支持开发者：

- ⭐ Star 这个项目
- 🐛 报告 Bug 或建议新功能
- 💝 赞助支持：[爱发电 JingJingZ](https://afdian.com/a/JingJingZ)

### 赞助方案

| 等级 | 月费 | 权益 |
|---|---|---|
| 🥤 随手一杯 | ¥5 | README 署名 + 月度进展 + 交流群 |
| 🚀 催更选手 | ¥15 | 以上 + 内测体验 + 每月点名 1 个功能优先排期 + Issue 优先回复 |
| 👑 金主爸爸 | ¥50 | 以上 + 每月 2 个需求直接排进计划 + 项目首页挂名字/Logo + 新工具首发通知 |

## 📄 License

本项目基于 [MIT License](LICENSE) 开源。

本项目使用了 [pdf2docx](https://github.com/dothinking/pdf2docx) 开源库（Apache 2.0 License）。

---

<div align="center">

Made with ❤️ and Python on Windows

[GitHub](https://github.com/12341141552204) · [爱发电](https://afdian.com/a/JingJingZ)

</div>
