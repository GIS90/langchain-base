from langchain_community.llms import Ollama
from typing import Optional, Any
import requests

class OllamaLocal:
    def __init__(self, 
                 model: str = "qwen3:8b",
                 base_url: str = "http://localhost:11434",
                 temperature: float = 0.7):
        self.llm = Ollama(
            model=model,
            base_url=base_url,
            temperature=temperature
        )

    def generate(self, prompt: str) -> str:
        """调用本地Ollama模型生成文本"""
        try:
            return self.llm.invoke(prompt)
        except requests.exceptions.ConnectionError:
            raise RuntimeError("无法连接到Ollama服务，请确认：\n"
                               "1. 已安装并运行Ollama\n"
                               "2. 服务地址正确（默认：http://localhost:11434）")

    def stream(self, prompt: str) -> Any:
        """流式输出生成结果"""
        return self.llm.stream(prompt)

# 使用示例
if __name__ == "__main__":
    ollama = OllamaLocal(model="qwen3:8b")
    response = ollama.generate("用三句话介绍量子计算")
    print(response)