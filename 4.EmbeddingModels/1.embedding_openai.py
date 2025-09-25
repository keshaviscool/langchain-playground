# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

print("env loaded")
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# embedding_openai = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
embedding_google = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", dimensions=32)

result1 = embedding_google.embed_query("hello keshav here")

result2 = embedding_google.embed_documents([
    "delhi is the capital of india",
    "kolkata is the capital of West Bengal",
    "Jaipur is the capital of Rajasthan"
])

print(result1, result2)