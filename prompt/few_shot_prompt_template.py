from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.prompts.few_shot import FewShotPromptTemplate


expamples = [
    {"input": "1", "output": "1"},
    {"input": "2", "output": "2"},
    {"input": "3", "output": "3"},
    {"input": "4", "output": "4"},
    {"input": "5", "output": "5"},
]

# 提示词追加示例：用于历史数据参考
expample_prompt = PromptTemplate(
    input_variables=["input", "output"], 
    template="输入: {input}, 输出: {output}"
)

prompt = FewShotPromptTemplate(
    examples=expamples,
    example_prompt=expample_prompt,
    prefix="你是一个数学老师，你需要回答学生的问题。",
    suffix="input: {input}, output: ",
    input_variables=["input"],
    example_separator="\n\n"
)

print(prompt.format(input="6"))