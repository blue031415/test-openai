from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": "俳句を一つ詠んで"}]
)

print(completion.choices[0].message.content)
