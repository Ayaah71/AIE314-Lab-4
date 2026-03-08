# sheglam_support.py
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

# Create docs folder
os.makedirs("sheglam_docs", exist_ok=True)

# Sheglam product manuals
lipstick = """
Sheglam Lipstick Guide
Common Issues: Color fading, Dry lips
Solutions: Apply lip balm before lipstick, Reapply every 4 hours, Store in cool place
Ingredients Info: Check packaging for allergens
"""
foundation = """
Sheglam Foundation Guide
Common Issues: Patchy application, Oxidation
Solutions: Shake bottle well, Apply primer, Choose correct shade for skin type
Expiration: 12 months after opening
"""
eyeshadow = """
Sheglam Eyeshadow Palette Manual
Common Issues: Powder fallout, Hard to blend
Solutions: Use primer, Tap brush before application, Use blending brushes
Storage: Keep away from humidity and direct sunlight
"""

# Save docs
for name, content in [("lipstick.txt", lipstick), ("foundation.txt", foundation), ("eyeshadow.txt", eyeshadow)]:
    with open(f"sheglam_docs/{name}", "w") as f:
        f.write(content)

# Load and split docs
documents = []
for file in os.listdir("sheglam_docs"):
    loader = TextLoader(f"sheglam_docs/{file}")
    documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Create embeddings & vector DB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(chunks, embeddings)
retriever = vectordb.as_retriever()

# Conversation memory
class ConversationMemory:
    def __init__(self):
        self.history = []

    def store(self, user_input, assistant_response):
        self.history.append((user_input, assistant_response))

    def get_context(self):
        context = ""
        for user, resp in self.history[-5:]:
            context += f"User: {user}\nAssistant: {resp}\n"
        return context

memory = ConversationMemory()

# Tools
def check_warranty(product):
    warranties = {
        "lipstick": "Warranty valid until 2026",
        "foundation": "Warranty valid until 2025",
        "eyeshadow": "Warranty valid until 2025"
    }
    return warranties.get(product.lower(), "Product not found")

def troubleshoot(issue):
    solutions = {
        "color fading": "Apply lip balm before lipstick and reapply every 4 hours",
        "dry lips": "Use lip balm before applying lipstick",
        "patchy application": "Shake foundation bottle well and use primer",
        "powder fallout": "Use primer and blending brushes"
    }
    return solutions.get(issue.lower(), "No troubleshooting guide available")

# LLM setup
generator = pipeline("text-generation", model="google/flan-t5-base", max_length=300)

class LocalLLMResponse:
    def __init__(self, content):
        self.content = content

def custom_llm_invoke(prompt):
    generated_text = generator(prompt)[0]["generated_text"]
    return LocalLLMResponse(generated_text)

# Chat system
def support_chat():
    print("Sheglam Makeup Support System")
    print("Type 'exit' to stop\n")
    
    while True:
        query = input("User: ")
        if query.lower() == "exit":
            break
        
        # Retrieve relevant docs
        docs = retriever.invoke(query)
        context_docs = "\n".join([doc.page_content for doc in docs])
        context_memory = memory.get_context()

        prompt = f"""
You are a Sheglam Makeup support assistant.

Conversation History:
{context_memory}

Relevant Documentation:
{context_docs}

User Question:
{query}

Provide step-by-step troubleshooting and recommendations.
"""
        response = custom_llm_invoke(prompt)
        memory.store(query, response.content)
        print("\nSupport:", response.content)

# Run chat
if __name__ == "__main__":
    support_chat()