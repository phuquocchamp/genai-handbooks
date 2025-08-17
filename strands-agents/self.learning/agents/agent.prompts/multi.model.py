from strands import Agent
from strands.session.file_session_manager import FileSessionManager
import uuid

# Create a session manager with a unique session ID
session_manager = FileSessionManager(
  session_id=uuid.uuid4().hex,
  storage_dir="./storage/sessions",  
)

agent = Agent(
  model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
  session_manager=session_manager,
  system_prompt=(
    "You are an expert Interview Coach specializing in technical interviews. "  
  ),
)


with open("./images/java-backend-developer.png", "rb") as fp:
  image_bytes = fp.read()

response = agent([
  {"text": "Review this Java backend developer's resume and provide feedback."},
  {
    "image": {
      "format": "png",
      "source" : {
        "bytes": image_bytes
      }
    }
  },
])