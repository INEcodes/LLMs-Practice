from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import time

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise Exception("API key missing! Please set GOOGLE_API_KEY in .env")

# Initialize client with API key
client = genai.Client(api_key=api_key)

# Create the File Search store
file_search_store = client.file_search_stores.create(
    config={"display_name": "your-fileSearchStore-name"}
)

# Upload and import a file into the File Search store
operation = client.file_search_stores.upload_to_file_search_store(
    file="sample.txt",
    file_search_store_name=file_search_store.name,
    config={"display_name": "display-file-name"},
)

# Wait for import to finish
while not operation.done:
    print("Importing file... please wait")
    time.sleep(5)
    operation = client.operations.get(operation)

print("File imported successfully!")

# Ask a question about the file
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Can you tell me my name? use sample txt file to answer.",
    config=types.GenerateContentConfig(
        tools=[
            {
                "file_search": {
                    "file_search_store_names": [file_search_store.name]
                }
            }
        ]
    )
)

print("\nResponse:\n", response.text)
