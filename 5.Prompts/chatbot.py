from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="AIzaSyD1-fKkFsETwtTmaKORyLOtwcuKx1BfWZU")

chat_history = [

]

while True:
    user_input = input("You: ")
    chat_history.append(f"User:  {user_input}")

    if user_input =="exit":
        print("BYE")
        break

    result = model.invoke(chat_history)
    chat_history.append(f"AI: {result.content}")
    print(f"AI: {result.content}")
