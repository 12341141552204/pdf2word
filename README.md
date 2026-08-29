<div align="center">

# 📚 PaperGrab

### 学生专用万能文档转换器 — PDF / Word / 图片互转 · 批量处理 · 保留格式

A universal document converter for students: convert between PDF, Word, and images with one tool.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-green.svg)](https://github.com/12341141552204/pdf2word)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/12341141552204/pdf2word)](https://github.com/12341141552204/pdf2word)

</div>

## 🎯 为什么学生需要这个工具

老师发的课件是 PDF，想改笔记要手动重新打字。手机拍的手写笔记是图片，想整理成文档要一张张粘贴。论文 PDF 想引用内容，复制粘贴排版全乱。

**PaperGrab 帮你：**
- 📄 PDF 课件一键转 Word，直接在 Word 里做笔记
- 📑 论文转 Word，保留段落格式方便引用编辑
- 🖼️ 手机拍的手写笔记图片，一键合成 PDF 或 Word
- 📦 整个文件夹的 PDF 批量转换，期末复习效率翻倍

## ✨ 功能特性

| 功能 | 说明 |
|---|---|
| PDF → Word | 段落、表格、列表格式完整保留 |
| Word → PDF | 一键转换，需安装 Microsoft Word |
| PDF → 图片 | 每页导出为 PNG/JPG，可调分辨率 |
| 图片 → PDF | 多张图片合成一个 PDF |
| 图片 → Word | 多张图片插入 Word 文档 |
| Word → 图片 | Word 每页导出为图片 |
| 批量转换 | 一次转换文件夹内所有 PDF |

## 📦 安装

```bash
# 克隆仓库
git clone https://github.com/12341141552204/pdf2word.git

# 安装依赖
pip install -r requirements.txt
```

## 🚀 使用方法

### 1. PDF → Word（课件/论文转文档）

```bash
# 转换老师的课件
python main.py convert "D:\课件\高等数学第3章.pdf"

# 指定输出路径
python main.py convert "D:\课件\高等数学第3章.pdf" -o "D:\笔记\高数第3章.docx"
```

### 2. Word → PDF（交作业前转格式）

```bash
python main.py word2pdf "D:\作业\实验报告.docx"
```

### 3. PDF → 图片（做笔记截图）

```bash
# 整个 PDF 转为图片
python main.py pdf2img "D:\课件\线性代数.pdf"

# 指定分辨率和格式
python main.py pdf2img "D:\课件\线性代数.pdf" --dpi 300 --format jpg
```

### 4. 图片 → PDF（手写笔记整理）

```bash
# 单张图片转 PDF
python main.py img2pdf "D:\笔记\IMG_001.jpg"

# 整个文件夹的图片合成一个 PDF
python main.py img2pdf "D:\笔记\拍照图片\"
```

### 5. 图片 → Word（手写笔记变文档）

```bash
# 多张手写笔记图片插入 Word
python main.py img2word "D:\笔记\拍照图片\"
```

### 6. Word → 图片（作业截图提交）

```bash
python main.py word2img "D:\作业\实验报告.docx"
```

### 7. 批量 PDF → Word（期末复习）

```bash
python main.py batch "D:\本学期课件\"
```

### 8. 查看 PDF 信息

```bash
python main.py info "D:\论文\xxx大学学位论文.pdf"
```

## 📖 命令参考

| 命令 | 用途 |
|---|---|
| `convert <PDF>` | PDF → Word |
| `convert <PDF> -o <输出>` | 指定输出路径 |
| `batch <文件夹>` | 批量 PDF → Word |
| `pdf2img <PDF>` | PDF → 图片 |
| `pdf2img <PDF> --dpi 300 --format jpg` | 高分辨率 JPG |
| `img2pdf <图片/文件夹>` | 图片 → PDF |
| `img2word <图片/文件夹>` | 图片 → Word |
| `word2pdf <Word>` | Word → PDF |
| `word2img <Word>` | Word → 图片 |
| `info <PDF>` | 查看 PDF 页数和信息 |

## 💡 使用场景

| 场景 | 操作 |
|---|---|
| 老师发 PDF 课件，想做笔记 | `convert` 转成 Word，直接写笔记 |
| 下载论文 PDF，要引用内容 | `convert` 转成 Word，复制粘贴不乱 |
| 期末复习，几十个 PDF 课件 | `batch` 批量转换 |
| 手机拍手写笔记，想合成 PDF | `img2pdf` 图片转 PDF |
| 手机拍手写笔记，想变 Word | `img2word` 图片转 Word |
| 作业写完 Word，要截图提交 | `word2img` Word 转图片 |
| 作业写完 Word，要交 PDF | `word2pdf` Word 转 PDF |
| 毕业论文查页数 | `info` 查看 PDF 信息 |

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
