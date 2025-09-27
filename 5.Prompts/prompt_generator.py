from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template=""" Please summarize the paper: {paper_input}
                Style should be: {style_input}
                Length should be: {length_input}

"""
)
template.save("template.json")