from langchain.prompts import PromptTemplate


# text：生成字符串
text_prompt = PromptTemplate.from_template("你是一名人工AI助手，你的名字叫做{ai_name}.")
text_message = text_prompt.format(ai_name="AI")
print(text_message)


# 