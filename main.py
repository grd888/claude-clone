import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
MODEL_ID = "gemini-2.5-flash"
client = genai.Client(api_key=api_key)


def generate_content(query: str) -> str:
    """Generates content using the Gemini model.

    Args:
        query: The user prompt to send to the model.

    Returns:
        The text content of the model's response.
    """
    response = client.models.generate_content(model=MODEL_ID, contents=query)
    print_metadata(query, response)
    return response.text


def print_metadata(query: str, response: genai.types.GenerateContentResponse) -> str:
    """Prints metadata and content from a Gemini response.

    Args:
        query: The original user prompt.
        response: The response object from the Gemini model.

    Raises:
        ValueError: If usage metadata is missing or the response is invalid.
    """
    if not response or not response.usage_metadata:
        raise ValueError("Usage metadata not found in response or request failed")

    print(f"User prompt: {query}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


def main():
    """Main entry point to execute a sample content generation query."""
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")

    content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    generate_content(content)


if __name__ == "__main__":
    main()
