#Creating the env variable for the API Key
from dotenv import load_dotenv
import os

#Langchain interaction libs
from langchain_core.messages import SystemMessage, HumanMessage
#Parser for string output
from langchain_core.output_parsers import StrOutputParser
#Langchain for OpenAi libs
from langchain_openai import ChatOpenAI
#Creates a template for a chat
from langchain_core.prompts import ChatPromptTemplate

#Loading API Key for connection
load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")

#Array to interact with OpenAI API
messages = [
    SystemMessage("Translate the following text to English"),
    HumanMessage("O que eu devo fazer?")
]

#Defining OpenAImodel
model = ChatOpenAI(model = "gpt-4o")
#Creating parser to extract only the string
parser = StrOutputParser()

#Catches the complete reply from OpenAI API
reply = model.invoke(messages)
#Parses only the string and print
textA = parser.invoke(reply)

#Defines the steps to create the chain
chainA = model | parser

#same output print(text) and print(chain.invoke(messages))
#chain.invoke(messages) receives the first parameter and delegates the return to the next step
print(textA)
print(chainA.invoke(messages))

#Defines a template for interacting with the API
messagesTemplate = ChatPromptTemplate.from_messages([
    ("system", "Translate the following text to {language}: "),
    ("user", "{userText}"),
])

#Defines new steps for the chain
chainB = messagesTemplate | model | parser
#Prints the reply
print(chainB.invoke({"language": "italian", "userText": "Nice to meet you!"}))