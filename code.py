from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")

messages = [
    SystemMessage("Translate the following text to English"),
    HumanMessage("O que eu devo fazer?")
]

model = ChatOpenAI(model = "gpt-4o")
parser = StrOutputParser()
chain = model | parser

# reply = model.invoke(messages)
# text = parser.invoke(reply)

messagesTemplate = ChatPromptTemplate.from_messages([
    ("system", "Translate the following text to {language}"),
    ("user", "{userText}"),
])

chain = messagesTemplate | model | parser

text = chain.invoke({"language": "german", "userText": "Is the translation working?"})

print(text)
