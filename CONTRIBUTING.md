# Contributing to PDF to Word Converter

Thank you for your interest in contributing!

## Getting Started

1. Fork this repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/pdf2word.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Install dependencies: `pip install pdf2docx`
5. Make your changes
6. Push: `git push origin feature/your-feature-name`
7. Open a Pull Request

## Development Setup

```bash
# Install dependencies
pip install pdf2docx

# Test the tool
py -3 main.py info sample.pdf
py -3 main.py convert sample.pdf
```

## Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Handle errors gracefully

## Reporting Bugs

Use the Bug Report template. Include:
- Python version (`py -3 --version`)
- Operating system
- PDF file details (pages, size, password-protected?)
- Error message
- Steps to reproduce

## Suggesting Features

Use the Feature Request template. Describe:
- The problem you're trying to solve
- Your proposed solution
- Use case

## Pull Request Checklist

- [ ] Code follows PEP 8
- [ ] Tested with various PDF files
- [ ] Updated README if needed
- [ ] Added CHANGELOG entry
- [ ] No unnecessary new dependencies
