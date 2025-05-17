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

router = APIRouter()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@router.post("/generate-sms")
async def generate_sms(product_name: str, tone: str):
    prompt = f"Write a {tone} SMS message promoting the product: {product_name}. Limit to 160 characters."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=160
    )
    return {"message": response.choices[0].text.strip()}