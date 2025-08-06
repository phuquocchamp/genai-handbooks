from strands import Agent
from strands.models import BedrockModel

# Create a Bedrock model with reasoning configuration
bedrock_model = BedrockModel(
    model_id="apac.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="ap-southeast-1",
    additional_request_fields={
        "thinking": {"type": "enabled", "budget_tokens": 4096}  # Minimum of 1,024
    },
)

# Create an agent with the reasoning-enabled model
agent = Agent(model=bedrock_model)

# Ask a question that requires reasoning
response = agent(
    "If a train travels at 120 km/h and needs to cover 450 km, how long will the journey take?"
)
