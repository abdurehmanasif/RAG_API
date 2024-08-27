
# RAG Chatbot API

This project implements a Retrieval-Augmented Generation (RAG) chatbot API using FastAPI, LangChain, and OpenAI's language models. The API allows users to upload documents and query them using natural language, providing responses based on the uploaded content or general knowledge from the LLM.

## Features

- Upload documents in PDF, DOCX, or CSV formats.
- Create and update a FAISS index for efficient document retrieval.
- Query the LLM directly when no documents are uploaded.
- Respond to user queries based on uploaded documents or LLM knowledge.

## Technologies Used

1. **FastAPI**: A modern web framework for building APIs with Python, known for its speed and ease of use.
2. **LangChain**: A framework for developing applications powered by language models, facilitating the integration of LLMs with other data sources.
3. **OpenAI**: For utilizing language models to generate responses based on user queries.
4. **FAISS**: A library for efficient similarity search and clustering of dense vectors, used for indexing and retrieving document embeddings.
5. **Pydantic**: For data validation and settings management using Python type annotations.

## File Structure

- **main.py**: This is the entry point of the application. It sets up the FastAPI app, defines the API endpoints for uploading documents and querying the chatbot, and handles requests and responses.
- **query_handler.py**: This file contains the `QueryHandler` class, which manages the FAISS index and the interactions with the OpenAI language model. It handles user queries, either retrieving answers from the FAISS index or querying the LLM directly if no documents have been uploaded.
- **file_uploader.py**: This file contains the `FileUploader` class, which handles the processing of uploaded files. It parses documents, splits them into chunks, and prepares them for indexing.
- **text_preprocessor.py**: This file contains the `TextPreprocessor` class, which preprocesses the text from document chunks by removing HTML tags, non-alphanumeric characters, and normalizing whitespace.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rag-chatbot-api.git
   cd rag-chatbot-api
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key in the `.env` file:

   - Create a `.env` file in the root of the project directory.
   - Add the following line to the `.env` file:

     ```plaintext
     OPENAI_API_KEY='your_openai_api_key'
     ```

   Replace `'your_openai_api_key'` with your actual OpenAI API key.

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the interactive API documentation (Swagger UI).

### Uploading Documents Using Postman

To upload a document using Postman:

1. Open Postman and create a new POST request.
2. Set the URL to `http://127.0.0.1:8000/upload/`.
3. Go to the "Body" tab and select "form-data".
4. Add a key named `file`, set its type to "File", and choose the document you want to upload (PDF, DOCX, or CSV).
5. Send the request by clicking the "Send" button.

### Querying the API Using Postman

To query the API using Postman:

1. Create a new POST request in Postman.
2. Set the URL to `http://127.0.0.1:8000/query/`.
3. Go to the "Body" tab and select "raw".
4. Set the format to "JSON".
5. Add the following JSON body:

   ```json
   {
       "query": "What are the skills of the candidate?"
   }
   ```

6. Send the request by clicking the "Send" button.

If documents have been uploaded, the API will respond with information based on the uploaded documents. If no documents have been uploaded, the API will provide a response based on the LLM's general knowledge.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- FastAPI
- LangChain
- OpenAI
- FAISS
```
