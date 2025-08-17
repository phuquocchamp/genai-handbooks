from strands import Agent
from strands.models import BedrockModel
from botocore.config import Config as BotocoreConfig


boto_config = BotocoreConfig(
    retries={"max_attempts": 3, "mode": "standard"},
    read_timeout=60,
    connect_timeout=60,
)

bedrock_model = BedrockModel(
    model_id="apac.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="ap-southeast-1",
    temperature=0.5,
    top_p=0.9,
    stop_sequences=["###", "END"],
    boto_client_config=boto_config,
)

agent = Agent(model=bedrock_model)

response = agent("Write a short story about an AI assistant")
