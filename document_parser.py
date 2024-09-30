import fitz  # PyMuPDF
import docx2txt
import pandas as pd

class DocumentParser:
    """Class to handle document parsing for PDF, DOCX, and CSV files."""

    def parse_pdf(self, file_path: str) -> str:
        """Parse a PDF file and return the text content."""
        try:
            doc = fitz.open(file_path)
            content = ""
            for page in doc:
                content += page.get_text()
            doc.close()
            return content
        except Exception as e:
            print(f"Failed to parse PDF {file_path}: {e}")
            return None

    def parse_docx(self, file_path: str) -> str:
        """Parse a DOCX file and return the text content."""
        try:
            return docx2txt.process(file_path)
        except Exception as e:
            print(f"Failed to parse DOCX {file_path}: {e}")
            return None
