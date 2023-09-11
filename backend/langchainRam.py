import os
import textwrap
import chromadb
import langchain
import openai
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import TextLoader

def print_response(response: str):
    print("\n".join(textwrap.wrap(response, width=100)))

os.environ["OPENAI_API_KEY"] = "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"

loader = TextLoader(file_path="backend\Rampr.txt")
#index_creator = VectorstoreIndexCreator()
#docsearch = index_creator.from_loaders([loader])
document= loader.load()
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(document, embeddings)
template = """
{context}
{question}
Answer:"""
 
prompt = PromptTemplate(template=template, input_variables=["context","question"])
print(
    prompt.format(
        context="""You're the person whose data is given. You are being asked \3
questions about youself by a political consulting organization so they \
can gauge your opinions on certain topics. Anwser the questions based on \
the information you know about yourself. Use your beliefs and use relevant information.""",
        question=""" What do you think bout the topic. Use only relevant experiences"""
    )
)
chain_type_kwargs = {"prompt": prompt}
chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=.9),
    chain_type="stuff",
    retriever=db.as_retriever(),
    chain_type_kwargs=chain_type_kwargs

)
query="Based on your opinoins would you like the tweet: AS your president I will raise drug prices."
print_response(chain.run(query))




