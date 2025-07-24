from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY =  os.getenv("API_KEY")

def run_llm(prompt: str, model: str = "gemini-2.0-flash") :
    client = genai.Client(api_key=API_KEY)
    
    response = client.models.generate_content(model=model, contents=prompt)
    
    return response.text
