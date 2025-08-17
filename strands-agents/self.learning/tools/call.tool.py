from strands import Agent


agent = Agent(
  model="apac.anthropic.claude-sonnet-4-20250514-v1:0",  
  tools=[weather_forecast],  
)