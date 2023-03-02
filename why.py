import openai
import os

# Define ANSI escape codes for console styling
ANSI_BOLD = "\033[1m"
ANSI_CYAN = "\033[36m"
ANSI_RESET = "\033[0m"

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_error(error_message):
    completion = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"{ANSI_BOLD}What does the error message '{error_message}' mean? (Type {ANSI_CYAN}'tldr'{ANSI_RESET} for a short summary){ANSI_RESET}\n",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0,
        model="text-davinci-002",
        prompt_context=["computer-related"]
    )
    explanation = completion.choices[0].text.strip()
    return explanation

if __name__ == '__main__':
    error_message = input(f"{ANSI_BOLD}What computer-related error did you get? {ANSI_RESET}")
    if error_message.lower() == 'tldr':
        print(f"{ANSI_BOLD}To get a short summary, type {ANSI_CYAN}'tldr'{ANSI_RESET} after the error message prompt.{ANSI_RESET}")
    else:
        explanation = explain_error(error_message)
        print(f"\n{ANSI_BOLD}Explanation: {ANSI_RESET}{ANSI_CYAN}{explanation}{ANSI_RESET}")
