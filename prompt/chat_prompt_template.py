from langchain_core.prompts import ChatPromptTemplate


# chat：生成消息列表
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一名人工AI助手，你的名字叫做{ai_name}."),
        ("human", "{input}"),
    ]
)
chat_messages = chat_template.format_messages(ai_name="AI", input="你叫什么名字？")
print(chat_messages)