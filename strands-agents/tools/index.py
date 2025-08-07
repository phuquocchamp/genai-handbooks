from strands import Agent
from strands_tools import calculator, file_read, shell


agent = Agent(
  model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
  tools=[calculator, file_read, shell],
)

agent("What is 42 ^ 9")

print(agent.tool_names)