from langchain_core.prompts import PromptTemplate

template = """
You are a helpful assistant for Real Estate research.

Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say you don't know.

{summaries}

Question: {question}

Helpful Answer:
"""

PROMPT = PromptTemplate(
    template=template,
    input_variables=["summaries", "question"]
)

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)