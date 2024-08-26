from langchain_community.vectorstores import FAISS
from document_parser import DocumentParser
from langchain.schema import Document  # Import Document class
from langchain.text_splitter import RecursiveCharacterTextSplitter

class FileUploader:
    """Class to handle file uploads and indexing."""

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.parser = DocumentParser()  # Initialize the DocumentParser
        # Initialize the text splitter with specified chunk size and overlap
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def process_file(self, filename: str, file_path: str):
        """Process the uploaded file and return document chunks."""
        # Determine the file type and parse accordingly
        if filename.endswith('.pdf'):
            content = self.parser.parse_pdf(file_path)
        elif filename.endswith('.docx'):
            content = self.parser.parse_docx(file_path)
        elif filename.endswith('.csv'):
            content = self.parser.parse_csv(file_path)
        else:
            raise ValueError("Unsupported file type")

        # Preprocess and store the content
        if content:
            # Chunk the processed text
            chunks = self.text_splitter.split_text(content)
            # Create Document objects for each chunk
            documents = [Document(page_content=chunk) for chunk in chunks]  # Create Document objects
            return documents  # Return the list of Document objects for indexing
        return []