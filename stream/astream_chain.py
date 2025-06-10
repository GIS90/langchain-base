from langchain_openai import ChatOpenAI
import asyncio
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_template(
    [
        ("system", "You are a helpful assistant."),
        ("user", "{question}"),
    ]
)
model = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()
chain = prompt | model | parser
async def async_stram():
    async for chunk in chain.astream({"question": "What is the capital of France?"}):
        print(chunk, end="", flush=True)
    print()
asyncio.run(async_stram())
