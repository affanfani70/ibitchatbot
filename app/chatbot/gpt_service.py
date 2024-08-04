import openai
import logging
from ..config import Config

openai.api_key = Config.OPENAI_API_KEY


def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response.choices[0].text.strip()
        if "ibit" in message.lower():
            return message
        return None
    except Exception as e:
        logging.error(f"Error calling GPT API: {e}")
        return None
