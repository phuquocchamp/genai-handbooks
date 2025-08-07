from strands import Agent

agent = Agent(
    model="apac.anthropic.claude-sonnet-4-20250514-v1:0",  # Optional:
)

agent("Hello, how can I assist you today?")  # Example usage of the agent

print(agent.messages)
