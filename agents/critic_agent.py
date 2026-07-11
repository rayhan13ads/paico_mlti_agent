import asyncio
from picoagents import Agent
from client import client

critic_agent = Agent(
    name="Critic Agent",
    description="Poetry critic who provides contructive feedback on haikus",
    instructions="""you are a haiku critic When you see a haiku, \
        provide 2-3 specific,actionable suggestions for improvement.\
        Be Constructive and brief.
        If satisfied with the haiku, respond with 'Approved'
        """,
    model_client=client,
)


async def test_critic():
    haiku = ("Cherry blossoms fall \n ",
    "Petals dancing in spring breeze \n",
    "Nature's gentle song"
    
    )
    response = await critic_agent.run(f"Please critque this haiku: \n {haiku} \n")
    print("========================")
    print(f"Critic says: \n{response}")
    print("========================")
    
