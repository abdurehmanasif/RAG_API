from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tempfile
from file_uploader import FileUploader
from query_handler import QueryHandler
from text_preprocessor import TextPreprocessor
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Allow CORS for all origins (modify as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
file_uploader = FileUploader()
query_handler = QueryHandler()
text_preprocessor = TextPreprocessor()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """API endpoint to upload files (CSV, PDF, DOCX) and create/update a FAISS index."""
    try:
        # Create a temporary file to save the uploaded file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            contents = await file.read()
            temp_file.write(contents)
            temp_file_path = temp_file.name

        # Process the file using FileUploader
        document_chunks = file_uploader.process_file(file.filename, temp_file_path)
        
        # Preprocess the document chunks
        preprocessed_chunks = text_preprocessor.preprocess_chunks(document_chunks)

        # Create or update the FAISS index
        query_handler.create_faiss_index(preprocessed_chunks)

        return {"message": "File uploaded and processed successfully."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

class QueryRequest(BaseModel):
    query: str

@app.post("/query/")
async def run_query(request: QueryRequest):
    """API endpoint to query the FAISS index and return relevant information."""
    try:
        # Process the query using QueryHandler
        response = query_handler.handle_query(request.query)
        # Extract the LLM response
        response = response["result"]["result"]

        # Return the extracted response
        return {"llm_response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.get("/")
def read_root():
    """Root endpoint for the RAG Chatbot."""
    return {"message": "Welcome to the RAG Chatbot API!"}