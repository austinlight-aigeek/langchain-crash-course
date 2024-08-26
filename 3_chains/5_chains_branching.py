from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnableBranch
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a thank you note for this positive feedback: {feedback}"),
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generate a repsonse addressing this negative feedback: {feedback}")
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a request for more details for this neutral response: {feedback}."),
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a message to escalate this feedback to a human agent: {feedback}."),
    ]
)

classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}.")
    ]
)

branches = RunnableBranch(
    (
        lambda x: "positive" in x,
        positive_feedback_template | model | StrOutputParser()
    ),
    (
        lambda x: "negative" in x,
        negative_feedback_template | model | StrOutputParser()
    ),
    (
        lambda x: "netural" in x,
        neutral_feedback_template | model | StrOutputParser()
    ),
    escalate_feedback_template | model | StrOutputParser()
)

classification_chain = classification_template | model | StrOutputParser()

chain = classification_chain | branches

review = "The product is excellent. I really enjoyed using it and found it very helpful."
result = chain.invoke({"feedback": review})

print(result)
