from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


# 用于把历史消息初始化传递给ai模型
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一名人工AI助手，你的名字叫做AI小王子."),
        MessagesPlaceholder("chat_history"),
        ("human", "你叫什么名称"),
    ]
)

message = prompt_template.invoke(
    {
        "chat_history": [HumanMessage(content="你好!"), AIMessage(content="你也好阿!")]
    }
)
print(message)