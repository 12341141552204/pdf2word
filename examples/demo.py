"""
PDF to Word Converter - Example Usage

Demonstrates all major features of the PDF to Word converter.
"""

import subprocess
import sys
import os

def run(args):
    """Run pdf2word with given arguments."""
    cmd = [sys.executable, "main.py"] + args
    print(f"\n{'='*60}")
    print(f"Running: {' '.join(cmd)}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    return result.returncode

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    os.chdir(parent_dir)

    print("PDF to Word Converter - Demo")
    print("=" * 60)

    # Example 1: View PDF info
    print("\n1. View PDF information:")
    print("   py -3 main.py info document.pdf")

    # Example 2: Convert single PDF
    print("\n2. Convert single PDF:")
    print("   py -3 main.py convert document.pdf")

    # Example 3: Batch convert
    print("\n3. Batch convert all PDFs in a folder:")
    print("   py -3 main.py batch ./pdfs/")

    # Example 4: Convert with custom output
    print("\n4. Convert to custom output path:")
    print("   py -3 main.py convert document.pdf -o output.docx")

    print("\n" + "=" * 60)
    print("Demo complete!")
    print("\nTo run with a real PDF file:")
    print(f"  py -3 main.py info your_file.pdf")
    print(f"  py -3 main.py convert your_file.pdf")
