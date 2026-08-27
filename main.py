#!/usr/bin/env python3
"""PDF to Word Converter - Batch convert PDF files to editable Word documents."""

import argparse
import os
import sys
from pathlib import Path

try:
    from pdf2docx import Converter
except ImportError:
    print("Error: pdf2docx not installed.")
    print("Run: pip install pdf2docx")
    sys.exit(1)


SUPPORTED_INPUT = ".pdf"


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


def main():
    parser = argparse.ArgumentParser(
        description="PDF to Word Converter - Batch convert PDF files to editable Word documents.",
        epilog="Examples:\n"
               "  python main.py convert document.pdf\n"
               "  python main.py convert document.pdf -o output.docx\n"
               "  python main.py batch \"C:\\Documents\"\n"
               "  python main.py batch \"C:\\Documents\" -o \"C:\\Output\"\n"
               "  python main.py info document.pdf",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    conv_parser = subparsers.add_parser("convert", help="Convert a single PDF to Word")
    conv_parser.add_argument("pdf", help="Path to the PDF file")
    conv_parser.add_argument("-o", "--output", help="Output Word file path (default: same name as PDF)")
    conv_parser.add_argument("--start", type=int, default=0, help="Start page number (0-based, default: 0)")
    conv_parser.add_argument("--end", type=int, default=None, help="End page number (exclusive)")

    batch_parser = subparsers.add_parser("batch", help="Batch convert all PDFs in a folder")
    batch_parser.add_argument("folder", help="Folder containing PDF files")
    batch_parser.add_argument("-o", "--output", help="Output folder for converted files")
    batch_parser.add_argument("--start", type=int, default=0, help="Start page number (0-based, default: 0)")
    batch_parser.add_argument("--end", type=int, default=None, help="End page number (exclusive)")

    info_parser = subparsers.add_parser("info", help="Show PDF file info (page count)")
    info_parser.add_argument("pdf", help="Path to the PDF file")

    args = parser.parse_args()

    if args.command == "convert":
        convert_single(args.pdf, args.output, start=args.start, end=args.end)
    elif args.command == "batch":
        convert_batch(args.folder, args.output, start=args.start, end=args.end)
    elif args.command == "info":
        list_pdf_info(args.pdf)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
