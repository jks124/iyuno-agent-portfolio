from fastapi import FastAPI
from pydantic import BaseModel
from .agent import Agent

app = FastAPI(title="Agentic Knowledge Triage")
agent = Agent()

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Agentic Knowledge Triage API"}

@app.post("/ask")
def ask(item: Question):
    return agent.answer(item.question)
