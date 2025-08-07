from strands import Agent
from strands.session.s3_session_manager import S3SessionManager
import boto3
import uuid


boto_session = boto3.Session(region_name="ap-southeast-1")

session_manager = S3SessionManager(
  session_id=uuid.uuid4().hex, 
  bucket="interview-questions-prep",
  prefix="dev/",
  boto_session=boto_session,
  region_name="ap-southeast-1",
)

agent = Agent(
  session_manager=session_manager,
  model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
)

agent("Tell me about AWS S3?")  # This conversation is persisted