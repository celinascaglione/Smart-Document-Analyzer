import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def extract_metadata_with_llm(text):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Please add it to your .env file."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
Extract the following metadata from the document text:

- document_id
- name
- company
- email
- city

Return only valid JSON with these exact keys:
document_id, name, company, email, city

Document text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    return json.loads(content)