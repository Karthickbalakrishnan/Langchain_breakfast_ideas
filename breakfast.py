import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load variables from .env into the environment
load_dotenv()

# Initialize model (temperature=0.7 for varied runs, or 0.0 for identical runs)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = (
    "Provide exactly 5 healthy, pure vegetarian South Indian breakfast ideas. "
    "Format them strictly as a numbered list, exactly one line per idea, with no preamble."
)

# Step 2 requirement: Inspect the raw message object returned by invoke()
reply = llm.invoke(prompt)
# This prints ONLY the clean text string:
print(reply.content)