import asyncio
from picoagents import Agent
from client import client

poet_agent = Agent(
    name="Poet Agent",
    description="Haiku poet.",
    instructions="You are a haiku poet.",
    model_client=client,
)

async def test_poet():
    response = await poet_agent.run("Write a haiku about cherry blossoms in spring.")
    print("========================")
    print(f"Poet says: \n{response}")
    print("========================")
    