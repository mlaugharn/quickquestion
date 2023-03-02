import openai
import os
import click

# Define ANSI escape codes for console styling
ANSI_BOLD = "\033[1m"
ANSI_GREEN = "\033[32m"
ANSI_RESET = "\033[0m"

openai.api_key = os.getenv("OPENAI_API_KEY")

@click.command()
@click.option('--tldr', '-t', is_flag=True, help=f"Get a short summary of the answer.")
@click.argument('question', required=True)
def generate_answer(tldr, question):
    if tldr:
        prompt = f"prompt_context=["computer-related"]|| {ANSI_BOLD}TLDR: How do I {question}?{ANSI_RESET}\n"
        max_tokens = 20
    else:
        prompt = f"{ANSI_BOLD}How do I {question}?{ANSI_RESET}\n"
        max_tokens = 100

    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0,
    )
    answer = completion.choices[0].text.strip()
    return answer

if __name__ == '__main__':
    answer = generate_answer()
    print(f"\n{ANSI_BOLD}Answer: {ANSI_RESET}{ANSI_GREEN}{answer}{ANSI_RESET}")
