# from datasets import load_dataset
# from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# classifier = pipeline('zero-shot-classification')
# text ="""This group consists of individuals who are on the cusp of becoming professional esports players. They may participate in semi-professional leagues or aspire to break into the professional scene.
# They seek controllers that offer a competitive edge and are willing to invest in equipment to improve their gameplay."""
# labels = ['young', 'old']
# result = classifier(text, labels)
# print(result)

def generate_target_market(productdescription,targetmarket,question): 
    llm = OpenAI(openai_api_key="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")
    template = """
{context}
{question}
Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["context","question"])
    formatted_prompt=  prompt.format(
        context=f""" I am building a product that {productdescription}. My target market is {targetmarket}""",
        question=f"""{question}"""
    )
    prediction= llm.predict(formatted_prompt)
    result = [x.strip() for x in prediction.split(',')]
    return result
productdescription="A new age video game controller that optimizes gaming"
targetmarket= """My target market is young esport gamers"""
question="""Can you  specify three specific groups within this target market focus and for each group include a paragrap description of each group and an age range"""
# print(generate_target_market(productdescription,targetmarket,question))

example_output=['Group 1: Amateur Esports Gamers: This group consists of young people aged between 16-25 who are just beginning to explore the world of esports. They may play in informal gaming communities and are interested in competitive gaming but lack the skill and experience of more professional players. They are looking for a controller that is easy to use and can help them improve their gaming skills.\n\nGroup 2: Professional Esports Gamers: This group consists of young people aged between 16-25 who are already established in the esports world. They are experienced esports players who are actively competing in tournaments and leagues. They are looking for a controller that is highly responsive and precise', 'allowing them to make the most of their gaming skills.\n\nGroup 3: Streamers and Content Creators: This group consists of young people aged between 16-25 who are primarily focused on creating content around their gaming experiences. They are interested in a controller that allows them to create and share exciting and engaging content for their viewers. They are looking for a controller that is reliable', 'customizable', 'and allows them to easily create dynamic gameplay videos.']

def scrape_gpt_target_market(output:str):
    output=output[0]
    list= output.splitlines()
    print(list)
    while("" in list):
      list.remove("")
    
scrape_gpt_target_market(example_output)