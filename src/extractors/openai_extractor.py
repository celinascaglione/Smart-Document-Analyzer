import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from extractors.base_extractor import BaseExtractor


load_dotenv()


class OpenAIExtractor(BaseExtractor):

    def __init__(self, model="gpt-4o-mini"):
        self.model = model

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Please add it to your .env file."
            )

        self.client = OpenAI(api_key=api_key)

    def extract(self, text):
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

        response = self.client.chat.completions.create(
            model=self.model,
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