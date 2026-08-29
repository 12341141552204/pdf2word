#!/usr/bin/env python3
"""DocConvert - Universal document converter: PDF, Word, Image inter-conversion."""

import argparse
import os
import sys
import tempfile
from pathlib import Path

try:
    import pymupdf
    sys.modules['fitz'] = pymupdf
    from pdf2docx import Converter
except ImportError:
    try:
        from pdf2docx import Converter
    except ImportError:
        print("Error: pdf2docx not installed.")
        print("Run: pip install pdf2docx")
        sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow not installed.")
    print("Run: pip install Pillow")
    sys.exit(1)

try:
    import docx
except ImportError:
    print("Error: python-docx not installed.")
    print("Run: pip install python-docx")
    sys.exit(1)


SUPPORTED_INPUT = ".pdf"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}


def convert_single(pdf_path, docx_path=None, start=0, end=None):
    """Convert a single PDF file to Word document."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        return False

    if pdf_path.suffix.lower() != SUPPORTED_INPUT:
        print(f"Error: Not a PDF file: {pdf_path}")
        return False

    if docx_path is None:
        docx_path = pdf_path.with_suffix(".docx")
    else:
        docx_path = Path(docx_path)

    print(f"Converting: {pdf_path.name} -> {docx_path.name}")

    try:
        cv = Converter(str(pdf_path))
        cv.convert(str(docx_path), start=start, end=end)
        cv.close()
        print(f"  Done! Saved to: {docx_path}")
        return True
    except Exception as e:
        print(f"  Error converting {pdf_path.name}: {e}")
        return False


def convert_batch(folder_path, output_folder=None, start=0, end=None):
    """Batch convert all PDF files in a folder."""
    folder = Path(folder_path)
    if not folder.exists():
        print(f"Error: Folder not found: {folder_path}")
        return

    pdf_files = sorted(f for f in folder.iterdir() if f.suffix.lower() == SUPPORTED_INPUT)

    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    print(f"Found {len(pdf_files)} PDF file(s)\n")

    if output_folder:
        out_dir = Path(output_folder)
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = folder

    success = 0
    failed = 0

    for i, pdf in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}]", end=" ")
        docx_path = out_dir / pdf.with_suffix(".docx").name
        ok = convert_single(pdf, docx_path, start=start, end=end)
        if ok:
            success += 1
        else:
            failed += 1

    print(f"\nResults: {success} succeeded, {failed} failed, {len(pdf_files)} total.")


def list_pdf_info(pdf_path):
    """Show basic info about a PDF file."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        return

    try:
        cv = Converter(str(pdf_path))
        print(f"File: {pdf_path.name}")
        print(f"Pages: {cv.page_count}")
        cv.close()
    except Exception as e:
        print(f"Error reading file: {e}")


def pdf_to_images(pdf_path, output_dir=None, dpi=150, fmt="png"):
    """Convert PDF pages to images using PyMuPDF."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        return

    if output_dir:
        out_dir = Path(output_dir)
    else:
        out_dir = pdf_path.parent / f"{pdf_path.stem}_images"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        doc = pymupdf.open(str(pdf_path))
        print(f"PDF: {pdf_path.name} ({doc.page_count} pages)")
        print(f"Output: {out_dir} (format: {fmt}, dpi: {dpi})\n")

        zoom = dpi / 72
        mat = pymupdf.Matrix(zoom, zoom)

        total = doc.page_count

        for i in range(total):
            page = doc[i]
            pix = page.get_pixmap(matrix=mat)
            img_name = f"{pdf_path.stem}_p{i+1:03d}.{fmt}"
            img_path = out_dir / img_name
            pix.save(str(img_path))
            print(f"  [{i+1}/{total}] {img_name}")

        doc.close()
        print(f"\nDone! {total} images saved to {out_dir}")
    except Exception as e:
        print(f"Error: {e}")


def images_to_pdf(input_path, output_path=None):
    """Combine multiple images into a single PDF using Pillow."""
    input_path = Path(input_path)

    if input_path.is_dir():
        imgs = sorted([f for f in input_path.iterdir() if f.suffix.lower() in IMAGE_EXTENSIONS])
    elif input_path.suffix.lower() in IMAGE_EXTENSIONS:
        imgs = [input_path]
    else:
        print(f"Error: Not an image or directory: {input_path}")
        return

    if not imgs:
        print("No images found.")
        return

    if output_path:
        out = Path(output_path)
    else:
        out = input_path.parent / "combined.pdf" if input_path.is_dir() else input_path.with_suffix(".pdf")

    print(f"Images: {len(imgs)}")
    print(f"Output: {out}\n")

    try:
        pil_images = []
        for i, img_path in enumerate(imgs, 1):
            img = Image.open(str(img_path))
            if img.mode == "RGBA":
                img = img.convert("RGB")
            pil_images.append(img)
            print(f"  [{i}/{len(imgs)}] {img_path.name} ({img.size[0]}x{img.size[1]})")

        pil_images[0].save(str(out), "PDF", save_all=True, append_images=pil_images[1:])
        print(f"\nDone! {len(imgs)} images combined into {out}")
    except Exception as e:
        print(f"Error: {e}")


def word_to_pdf(word_path, output_path=None):
    """Convert Word document to PDF using Microsoft Word COM automation."""
    word_path = Path(word_path)
    if not word_path.exists():
        print(f"Error: File not found: {word_path}")
        return

    if word_path.suffix.lower() not in (".doc", ".docx"):
        print(f"Error: Not a Word file: {word_path}")
        return

    if output_path:
        out = Path(output_path)
    else:
        out = word_path.with_suffix(".pdf")

    print(f"Word: {word_path.name}")
    print(f"Output: {out}\n")

    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(str(word_path.resolve()))
        doc.SaveAs(str(out.resolve()), FileFormat=17)
        doc.Close()
        word.Quit()
        print(f"Done! {out}")
    except ImportError:
        print("Error: pywin32 not installed.")
        print("Run: pip install pywin32")
    except Exception as e:
        print(f"Error: {e}")
        print("Note: Microsoft Word must be installed for Word → PDF conversion.")


def images_to_word(input_path, output_path=None):
    """Insert multiple images into a Word document using python-docx."""
    input_path = Path(input_path)

    if input_path.is_dir():
        imgs = sorted([f for f in input_path.iterdir() if f.suffix.lower() in IMAGE_EXTENSIONS])
    elif input_path.suffix.lower() in IMAGE_EXTENSIONS:
        imgs = [input_path]
    else:
        print(f"Error: Not an image or directory: {input_path}")
        return

    if not imgs:
        print("No images found.")
        return

    if output_path:
        out = Path(output_path)
    else:
        out = input_path.parent / "images.docx" if input_path.is_dir() else input_path.with_suffix(".docx")

    print(f"Images: {len(imgs)}")
    print(f"Output: {out}\n")

    try:
        doc = docx.Document()
        for i, img_path in enumerate(imgs, 1):
            doc.add_picture(str(img_path), width=docx.shared.Inches(6))
            doc.add_paragraph(f"Image {i}: {img_path.name}")
            print(f"  [{i}/{len(imgs)}] {img_path.name}")
        doc.save(str(out))
        print(f"\nDone! {len(imgs)} images inserted into {out}")
    except Exception as e:
        print(f"Error: {e}")


def word_to_images(word_path, output_dir=None, dpi=150, fmt="png"):
    """Convert Word to images via PDF (Word → PDF → Images)."""
    word_path = Path(word_path)
    if not word_path.exists():
        print(f"Error: File not found: {word_path}")
        return

    if output_dir:
        out_dir = Path(output_dir)
    else:
        out_dir = word_path.parent / f"{word_path.stem}_images"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Step 1: Word → PDF")
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False, dir=str(out_dir)) as tmp:
        tmp_pdf = Path(tmp.name)

    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(str(word_path.resolve()))
        doc.SaveAs(str(tmp_pdf.resolve()), FileFormat=17)
        doc.Close()
        word.Quit()
    except Exception as e:
        print(f"  Word → PDF failed: {e}")
        print("  Note: Microsoft Word must be installed.")
        if tmp_pdf.exists():
            tmp_pdf.unlink()
        return

    print("Step 2: PDF → Images")
    pdf_to_images(tmp_pdf, out_dir, dpi=dpi, fmt=fmt)
    tmp_pdf.unlink()


def main():
    parser = argparse.ArgumentParser(
        description="DocConvert - Universal document converter (PDF/Word/Image inter-conversion).",
        epilog="Examples:\n"
               "  PDF → Word:  python main.py convert document.pdf\n"
               "  Word → PDF:  python main.py word2pdf document.docx\n"
               "  PDF → Image: python main.py pdf2img document.pdf\n"
               "  Image → PDF: python main.py img2pdf photo.jpg\n"
               "  Image → Word: python main.py img2word photo.jpg\n"
               "  Word → Image: python main.py word2img document.docx\n"
               "  Batch PDF → Word: python main.py batch \"C:\\Documents\"\n"
               "  PDF info: python main.py info document.pdf",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    conv_parser = subparsers.add_parser("convert", help="PDF → Word")
    conv_parser.add_argument("pdf", help="Path to the PDF file")
    conv_parser.add_argument("-o", "--output", help="Output Word file path")
    conv_parser.add_argument("--start", type=int, default=0, help="Start page (0-based)")
    conv_parser.add_argument("--end", type=int, default=None, help="End page (exclusive)")

    batch_parser = subparsers.add_parser("batch", help="Batch convert all PDFs in a folder to Word")
    batch_parser.add_argument("folder", help="Folder containing PDF files")
    batch_parser.add_argument("-o", "--output", help="Output folder")
    batch_parser.add_argument("--start", type=int, default=0, help="Start page (0-based)")
    batch_parser.add_argument("--end", type=int, default=None, help="End page (exclusive)")

    info_parser = subparsers.add_parser("info", help="Show PDF file info (page count)")
    info_parser.add_argument("pdf", help="Path to the PDF file")

    p2i_parser = subparsers.add_parser("pdf2img", help="PDF → Images (PNG/JPG)")
    p2i_parser.add_argument("pdf", help="Path to the PDF file")
    p2i_parser.add_argument("-o", "--output", help="Output directory")
    p2i_parser.add_argument("--dpi", type=int, default=150, help="Resolution DPI (default: 150)")
    p2i_parser.add_argument("--format", choices=["png", "jpg"], default="png", help="Image format (default: png)")

    i2p_parser = subparsers.add_parser("img2pdf", help="Images → PDF (single or folder)")
    i2p_parser.add_argument("input", help="Image file or folder of images")
    i2p_parser.add_argument("-o", "--output", help="Output PDF path")

    w2p_parser = subparsers.add_parser("word2pdf", help="Word → PDF (requires Microsoft Word)")
    w2p_parser.add_argument("word", help="Path to the Word file (.doc/.docx)")
    w2p_parser.add_argument("-o", "--output", help="Output PDF path")

    i2w_parser = subparsers.add_parser("img2word", help="Images → Word (single or folder)")
    i2w_parser.add_argument("input", help="Image file or folder of images")
    i2w_parser.add_argument("-o", "--output", help="Output Word path")

    w2i_parser = subparsers.add_parser("word2img", help="Word → Images (requires Microsoft Word)")
    w2i_parser.add_argument("word", help="Path to the Word file (.doc/.docx)")
    w2i_parser.add_argument("-o", "--output", help="Output directory")
    w2i_parser.add_argument("--dpi", type=int, default=150, help="Resolution DPI (default: 150)")
    w2i_parser.add_argument("--format", choices=["png", "jpg"], default="png", help="Image format (default: png)")

    args = parser.parse_args()

    if args.command == "convert":
        convert_single(args.pdf, args.output, start=args.start, end=args.end)
    elif args.command == "batch":
        convert_batch(args.folder, args.output, start=args.start, end=args.end)
    elif args.command == "info":
        list_pdf_info(args.pdf)
    elif args.command == "pdf2img":
        pdf_to_images(args.pdf, args.output, dpi=args.dpi, fmt=args.format)
    elif args.command == "img2pdf":
        images_to_pdf(args.input, args.output)
    elif args.command == "word2pdf":
        word_to_pdf(args.word, args.output)
    elif args.command == "img2word":
        images_to_word(args.input, args.output)
    elif args.command == "word2img":
        word_to_images(args.word, args.output, dpi=args.dpi, fmt=args.format)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
