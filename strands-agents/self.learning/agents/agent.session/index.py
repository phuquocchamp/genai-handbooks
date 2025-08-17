from strands import Agent
from strands.session.file_session_manager import FileSessionManager

# Create a session manager with a unique session ID
session_manager = FileSessionManager(
  session_id="test-session",
  storage_dir="./storage/sessions",  
)

# Create an agent with the session manager
agent = Agent(
  session_manager=session_manager,
  model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
)

# Use the agent - all messages and state are automatically persisted
agent("How are you today ?")  # This conversation is persisted