import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)

result = model.invoke("What is 81 divided by 9?")

print("Full result:")
print(result)
print("Content only:")
print(result.content)