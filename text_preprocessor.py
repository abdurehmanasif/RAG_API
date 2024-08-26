import re
from langchain.schema import Document  # Import Document class

class TextPreprocessor:
    """Class to handle text preprocessing."""

    def preprocess_chunks(self, documents: list) -> list:
        """Preprocess a list of Document objects."""
        preprocessed_documents = []
        
        for doc in documents:
            # Preprocess the text in each Document
            text = doc.page_content
            
            # Remove HTML tags
            text = re.sub(r'<[^>]+>', '', text)
            # Replace newlines and carriage returns with a space
            text = text.replace('\n', ' ').replace('\r', '').strip()
            # Convert to lowercase
            text = text.lower()
            # Remove non-alphanumeric characters
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
            # Normalize whitespace
            text = re.sub(r'\s+', ' ', text)
            
            # Create a new Document with the preprocessed text
            preprocessed_documents.append(Document(page_content=text))
        
        return preprocessed_documents