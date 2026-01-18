import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
MODEL_ID = "gemini-2.5-flash"
client = genai.Client(api_key=api_key)


def main():
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")

    content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(model=MODEL_ID, contents=content)
    print(response.text)


if __name__ == "__main__":
    main()
