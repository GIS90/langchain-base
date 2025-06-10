from langchain_openai import ChatOpenAI


model = ChatOpenAI(model="gpt-3.5-turbo")

chunks = list()
for chunk in model.stream("What is the capital of France?"):
    chunks.append(chunk)