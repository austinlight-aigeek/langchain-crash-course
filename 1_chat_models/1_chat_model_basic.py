import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

openai_api_key = "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"

model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)

result = model.invoke("What is 81 divided by 9?")

print("Full result:")
print(result)
print("Content only:")
print(result.content)