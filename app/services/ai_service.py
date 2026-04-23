from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_document(prompt: str):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    return response.output_text