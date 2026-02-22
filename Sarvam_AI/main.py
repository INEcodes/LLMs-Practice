import os
from sarvamai import SarvamAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

# Initialize client with your API key (get from Sarvam dashboard)
client = SarvamAI(api_subscription_key=os.getenv("SarvamAI_API_KEY"))

# Example chat request
response = client.chat.completions(
    messages=[
        {"role": "user", "content": "Hello, what is the capital of India?"}
    ]
)

# Print the response
print(response.choices[0].message.content)
