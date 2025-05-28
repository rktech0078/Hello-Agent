from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")

if not openrouter_api_key:
    raise ValueError("GEMINI API KEY IS NOOT CONNECTED WITH ENV FILE `ERROR` ")


external_client = AsyncOpenAI (
    api_key = openrouter_api_key,
    base_url = "https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    model = "opengvlab/internvl3-14b:free",
    openai_client = external_client
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True 
)

agent = Agent(
    name = "Assistant",
    instructions = "You are a helpful assistant",
    model = model
)

user_message = str(input("Enter your message here for AI AGENT: "))

result = Runner.run_sync(
    agent,
    user_message,
    run_config = config
)

print(result.final_output)