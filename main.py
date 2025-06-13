import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_prompt = sys.argv[1]

args = sys.argv[2:]

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]


def main():
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )
    except:
        print("Provide a prompt first e.g.: `python3 main.py 'Hello'`")
        sys.exit(1)

    prompt_token = response.usage_metadata.prompt_token_count
    response_token = response.usage_metadata.candidates_token_count

    print(response.text)

    if argument_reader(args):
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_token}")
        print(f"Response tokens: {response_token}")


def argument_reader(args):
    if "--verbose" in args:
        return True
    return False


if __name__ == "__main__":
    main()
