import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
MODEL_ID = "gemini-2.5-flash"
client = genai.Client(api_key=api_key)


def generate_content(query: str, verbose: bool = False) -> str:
    """Generates content using the Gemini model.

    Args:
        query: The user prompt to send to the model.

    Returns:
        The text content of the model's response.
    """
    response = client.models.generate_content(model=MODEL_ID, contents=query)
    if verbose:
        print_metadata(query, response)
    return response.text


def print_metadata(query: str, response: types.GenerateContentResponse) -> str:
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

    parser = argparse.ArgumentParser(description="Chat with an AI assistant")
    parser.add_argument("user_prompt", type=str, help="The user prompt")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_content(messages, verbose=args.verbose)


if __name__ == "__main__":
    main()
