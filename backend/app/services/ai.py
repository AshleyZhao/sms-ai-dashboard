from fastapi import APIRouter
from openai import OpenAI
from dotenv import load_dotenv
import os

# Get the parent directory of the current file
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Build the path to the .env file in the parent directory
dotenv_path = os.path.join(parent_dir, '.env')

# Load the .env file
load_dotenv(dotenv_path=dotenv_path)

# Optional: check if it worked
print("API Key:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

@router.post("/generate-sms")
async def generate_sms(product_name: str, tone: str):
    # Define your prompt
    prompt = f"Write a {tone} SMS message promoting the product: {product_name}. Limit to 160 characters."
    
    # Call the OpenAI API using the new client (for GPT-4 or GPT-3.5 models)
    response = await client.responses.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
        instructions=prompt,  # The instructions for the model
        input=prompt,  # You pass the prompt here as input (empty string is fine)
    )
    
    # Return the generated SMS message
    return response.output_text.strip()