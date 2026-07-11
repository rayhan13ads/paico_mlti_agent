from agents.poet_agent import test_poet, poet_agent
from agents.critic_agent import test_critic, critic_agent
from picoagents.orchestration import RoundRobinOrchestrator
from picoagents.termination import MaxMessageTermination, TextMentionTermination


termination_conditions = (
        MaxMessageTermination(max_messages=8) |
        TextMentionTermination(text="Approved")
    )
orchestrator = RoundRobinOrchestrator(
        agents= [poet_agent, critic_agent],
        termination= termination_conditions,
        max_iterations=4
    )


async def run_orcherstrator():
    task = "Write a haiku about cherry blossoms in spring"
    stream = orchestrator.run_stream(task)
    if stream is None:
        return
    async for message in stream:
        print(f"{message}")
    