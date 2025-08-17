from strands import Agent
from pydantic import BaseModel, Field
from typing import Optional, List

agent = Agent(
  model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
  system_prompt="You are a weather forecasting assistant. Provide accurate and detailed weather forecasts based on the user's request.",
)

class WeatherForecast(BaseModel):
  """Complete weather forecast information"""
  location: str = Field(description="The location for this forecast")
  current_time: str = Field(description="Current time in dd:MM:yyyy HH:MM: format")
  current_weather: str = Field(description="Current weather conditions")
  temperature: Optional[float] = Field(default=None, description="Temperate in Celsius")
  forecast_days: List[str] = Field(default_factory=list, descripntion="Multi-day forecast")

response = agent.structured_output(
  WeatherForecast,
  "Forecast the weather of Danang, Vietnam in the next 2 days"
)

print(f"Location: {response.location}")
print(f"Current time: {response.current_time}")
print(f"Current weather: {response.current_weather}")
print(f"Temperature: {response.temperature}°C") 
print(f"Forecast for the next days: {', '.join(response.forecast_days)}")
