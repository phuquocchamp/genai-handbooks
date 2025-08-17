from strands import Agent

agent = Agent(
  model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
  system_prompt=(
     "You are a financial advisor specialized in retirement planning. "
      "Use tools to gather information and provide personalized advice. "
      "Always explain your reasoning and cite sources when possible."
  )
)

response = agent(
  "What are the best investment strategies for retirement?"
)

