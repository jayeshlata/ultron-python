import os
import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the new Gemini Client
genai_client = genai.Client(api_key=api_key)

class GeminiEmbeddingFunction(chromadb.EmbeddingFunction):
    def __call__(self, input):
        response = genai_client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=input
        )
        if hasattr(response, 'embeddings'):
             return [e.values for e in response.embeddings]
        return [response.embedding.values]
    
    def name(self):
        return "GeminiEmbeddingFunction"

# Set up local ChromaDB
client = chromadb.PersistentClient(path="./spooky_memory")

collection = client.get_or_create_collection(
    name="long_term_memory",
    embedding_function=GeminiEmbeddingFunction()
)

def remember_fact(fact: str) -> str:
    """Saves a piece of information about the user or the world to Spooky's memory."""
    import uuid
    id_str = str(uuid.uuid4())
    collection.add(
        documents=[fact],
        ids=[id_str]
    )
    return f"👻 My digital brain has absorbed this fact: '{fact}'"

def search_memory(query: str) -> str:
    """Searches Spooky's memory for information related to the query."""
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    
    if not results['documents'] or not results['documents'][0]:
        return "👻 I searched the shadows of my memory, but found nothing."
    
    memories = "\n".join(results['documents'][0])
    return f"👻 Here is what I remember about '{query}':\n{memories}"
