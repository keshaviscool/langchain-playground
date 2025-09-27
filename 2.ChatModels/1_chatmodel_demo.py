# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=1.2, # more the temperature, more the randomness
    # max_tokens=10 # roughly these are number of words 


)

result = model.invoke("hello")

print(result.content)