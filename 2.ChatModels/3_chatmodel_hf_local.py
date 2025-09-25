from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline # BaseChatModel in langchain
from dotenv import load_dotenv

import os
os.environ["HF_HOME"] = "D/<asdasdasd>" #iit kgp

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", #model download will take place in our machine
    task="text-generation",
    pipeline_kwargs=dict( #imp
        max_new_tokens=100,
        temperature=0.5
    )
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("what is the capital of india?")
print(result.content)


