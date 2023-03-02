import openai
import os

# Define ANSI escape codes for console styling
ANSI_BOLD = "\033[1m"
ANSI_GREEN = "\033[32m"
ANSI_RESET = "\033[0m"

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(question):
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{ANSI_BOLD}{question} (Type {ANSI_GREEN}'tldr'{ANSI_RESET} for a short summary){ANSI_RESET}\n",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0,
    )
    answer = completion.choices[0].text.strip()
    return answer

if __name__ == '__main__':
    question = input(f"{ANSI_BOLD}What computer-related question do you have? {ANSI_RESET}")
    if question.lower() == 'tldr':
        print(f"{ANSI_BOLD}To get a short summary, type {ANSI_GREEN}'tldr'{ANSI_RESET} after the question prompt.{ANSI_RESET}")
    else:
        answer = generate_answer(question)
        print(f"\n{ANSI_BOLD}Answer: {ANSI_RESET}{ANSI_GREEN}{answer}{ANSI_RESET}")
