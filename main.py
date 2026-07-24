from fastapi import FastAPI
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase


load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ecommerce.db")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile")

db = SQLDatabase.from_uri(DATABASE_URL)

toolkit = SQLDatabaseToolkit(db = db, llm = llm)

agent_executor = create_sql_agent(
        llm = llm,
        toolkit = toolkit,
        max_iterations = 15,
        max_execution_time = 60,
        top_k = 10,
        verbose = True
    )

def run_pipeline(user_query:str) -> str:

    result = agent_executor.invoke({"input": user_query})

    return result["output"]


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/analyze/{query}")
async def get(query: str):
    response =  run_pipeline(query)
    return {"query": query, "result": response}