import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from functions.call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        ),
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    if not response.function_calls:
        print("Response:")
        print(response.text)
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)
        if not function_call_result.parts:
            raise RuntimeError("Function call result appears to be malformed")
        function_response = function_call_result.parts[0].function_response
        if not function_response.name:
            raise RuntimeError("Function response name is missing")

        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")


if __name__ == "__main__":
    main()
