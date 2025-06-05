from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


# 采用Message模板方式
chat_template2 = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="你是一名人工AI助手，你的名字叫做AI小王子"),
        HumanMessage(content="你好。"),
        AIMessage(content="你好，我叫AI小王子。"),
        HumanMessage(content="{input}"),
    ]
)
chat_messages2 = chat_template2.format_messages(ai_name="AI", input="你叫什么名字？")
print(chat_messages2)

