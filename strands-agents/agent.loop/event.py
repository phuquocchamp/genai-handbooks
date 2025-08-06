from strands import Agent
from strands_tools import calculator

agent = Agent(
    tools=[calculator],
    system_prompt="You are a helpful assistant that provides concise responses.",
    model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
)

result = agent("Calculate the sum of 5 and 10.")

print(f"Result: {result}")
