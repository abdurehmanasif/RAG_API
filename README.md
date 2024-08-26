# RAG Chatbot API

This project implements a Retrieval-Augmented Generation (RAG) chatbot API using FastAPI, LangChain, and OpenAI's language models. The API allows users to upload documents and query them using natural language, providing responses based on the uploaded content or general knowledge from the LLM.

## Features

- Upload documents in PDF, DOCX, or CSV formats.
- Create and update a FAISS index for efficient document retrieval.
- Query the LLM directly when no documents are uploaded.
- Respond to user queries based on uploaded documents or LLM knowledge.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python.
- **LangChain**: A framework for developing applications powered by language models.
- **OpenAI**: For utilizing language models to generate responses.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rag-chatbot-api.git
   cd rag-chatbot-api

Create a virtual environment (optional but recommended):
bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
bash
pip install -r requirements.txt

Set your OpenAI API key in the environment variable:
bash
export OPENAI_API_KEY='your_openai_api_key'  # On Windows use `set OPENAI_API_KEY='your_openai_api_key'`

Usage
Start the FastAPI server:
bash
uvicorn main:app --reload

Open your browser and navigate to http://127.0.0.1:8000/docs to access the interactive API documentation (Swagger UI).
Uploading Documents
To upload a document, send a POST request to /upload/ with the file included in the form data. Supported file types are PDF, DOCX, and CSV.
Querying the API
To query the API, send a POST request to /query/ with a JSON body containing the query string. For example:
json
{
    "query": "What are the skills of the candidate?"
}

If no documents have been uploaded, the API will respond with information based on the LLM's general knowledge.
Example
Here’s an example of how to upload a document and then query the API:
Upload a document:
bash
curl -X POST "http://127.0.0.1:8000/upload/" -F "file=@path_to_your_file.pdf"

Query the API:
bash
curl -X POST "http://127.0.0.1:8000/query/" -H "Content-Type: application/json" -d '{"query": "What is the summary of the document?"}'

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements
FastAPI
LangChain
OpenAI
FAISS
