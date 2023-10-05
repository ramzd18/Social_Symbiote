from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI


def generate_relevant_memories(question): 
    llm = OpenAI(openai_api_key="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")
    template = """
{context}
{question}
Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["context","question"])
    formatted_prompt=  prompt.format(
        context=""" You are given general information about a person and some of thier characteristics. Your goal is to generate a list of activities and memories the person could potentially have. Do not put numbers in the list and seperate by commas""",
        question=f"""{question}"""
    )
    prediction= llm.predict(formatted_prompt)
    result = [x.strip() for x in prediction.split(',')]
    return result




# generate_relevant_memories("Generate memories for Ram. Ram is a college student who loves to watch football and play sports. He specifically spends a lot of money on basketball hoops and spikeball nets. Start the memories with Ram's name. Make each memory a full sentence")