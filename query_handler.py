from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.faiss import DistanceStrategy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Access the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class QueryHandler:
    """Class to handle queries against the FAISS index."""

    def __init__(self):
        self.faiss_index = None  # This will hold the FAISS index
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.turbo_llm = ChatOpenAI(
            temperature=0,
            model_name='gpt-4o-mini',  # Use the appropriate model
            openai_api_key=OPENAI_API_KEY  
        )
        self.qa_chain = None  # Initialize qa_chain as None

    def initialize_qa_chain(self):
        """Initialize the RetrievalQA chain if the FAISS index is available."""
        if self.faiss_index is not None:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.turbo_llm,
                chain_type="stuff",
                retriever=self.faiss_index.as_retriever(),
                return_source_documents=True
            )

    def create_faiss_index(self, document_chunks):
        """Create a FAISS index from document chunks."""
        if document_chunks:
            # Create FAISS index with cosine distance strategy
            self.faiss_index = FAISS.from_documents(
                document_chunks,
                self.embedding_model,
                distance_strategy=DistanceStrategy.COSINE
            )
            self.faiss_index.save_local("faiss_index")  # Save the FAISS index locally
            self.initialize_qa_chain()  # Initialize the QA chain after creating the index
            print("FAISS index created and QA chain initialized.")
        else:
            print("No document chunks provided.")

    def load_faiss_index(self):
        """Load the FAISS index from local storage."""
        print("Loading FAISS index...")
        self.faiss_index = FAISS.load_local("faiss_index", self.embedding_model, allow_dangerous_deserialization=True)
        self.initialize_qa_chain()  # Initialize the QA chain after loading the index
        print("FAISS index loaded and QA chain initialized.")

    def handle_query(self, query: str):
        """Handle a query and return the response."""
        if self.faiss_index is None:
            # If no documents have been uploaded, query the LLM directly
            response = self.turbo_llm(query)  # Query the LLM directly
            return {
                "result": {
                    "query": query,
                    "result": response,
                    "source_documents": []
                }
            }

        # If the FAISS index is available, proceed with the query
        try:
            # Perform a similarity search to get the most relevant chunks
            results = self.faiss_index.similarity_search_with_relevance_scores(query, k=3)

            # Check if results are returned in the expected format
            if not results:
                return {"result": "No relevant documents found."}

            # Concatenate the top chunks
            context = " ".join([res.page_content for res, score in results])

            # Define the prompt template
            review_template = """\
            Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
            Context: {relevant_text}
            Question: {query}
            Helpful Answer:"""
            
            prompt_template = ChatPromptTemplate.from_template(review_template)

            # Invoke the QA chain
            response = self.qa_chain.invoke(prompt_template.format(relevant_text=context, query=query))

            # Return the response as a dictionary with a single key
            return {"result": response}
        except Exception as e:
            raise RuntimeError(f"Error running query: {str(e)}")
