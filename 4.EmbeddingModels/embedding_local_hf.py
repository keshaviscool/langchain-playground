from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

text = "Delhi is the capital of India"

vector = embeddings.embed_query(text)
print(vector)