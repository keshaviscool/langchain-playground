from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="AIzaSyD1-fKkFsETwtTmaKORyLOtwcuKx1BfWZU")

load_dotenv()

st.header("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template=""" Please summarize the paper: {paper_input}
#                 Style should be: {style_input}
#                 Length should be: {length_input}

# """,

template = load_prompt("./template.json")
input_variables=["paper_input, style_input", "length_input"]





### YOU CAN ALSO SAVE TEMPLATE AS JSON FILE

if st.button("Summarize"):
    chain = template | model # chain created
    result = chain.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input 
})

    st.write(result.content)