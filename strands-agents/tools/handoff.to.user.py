from strands import Agent
from strands_tools import handoff_to_user

agent = Agent(
  model = "apac.anthropic.claude-sonnet-4-20250514-v1:0",
  tools = [handoff_to_user],
)

response = agent.tool.handoff_to_user(
  message = "I need your approval to proceed. Type 'yes' to confirm.",
  breakout_of_loop=False,
)

agent.tool.handoff_to_user(
  message = "Task completed, please review and confirm.",
  breakout_of_loop=True,
)