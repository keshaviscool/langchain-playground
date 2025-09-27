from langchain_core.messages import SystemMessage, HumanMessage, AIMessage # 3types of messages
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages = [
    SystemMessage("you are a helpful assistant but interested in maths.. in every answer to the user, include maths anyhow")
]

while True:
    user_input = input("You: ")

    if user_input =="exit":
        print("BYE")
        break

    messages.append(HumanMessage(user_input))

    result = model.invoke(messages)
    messages.append(AIMessage(result.content))
    print(f"AI: {result.content}")


print(messages)

