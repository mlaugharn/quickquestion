import openai
import os
import click

# Define ANSI escape codes for console styling
ANSI_BOLD = "\033[1m"
ANSI_GREEN = "\033[32m"
ANSI_RESET = "\033[0m"

openai.api_key = os.getenv("OPENAI_API_KEY")

@click.command()
@click.option('--tldr', '-t', is_flag=True, help='Provide a short summary')
@click.argument('question', type=str)
def generate_answer(tldr, question):
    if tldr:
        max_tokens = 50
    else:
        max_tokens = 100

    prompt = f"{ANSI_BOLD}Why is {question}?{ANSI_RESET}\n"
    if tldr:
        prompt += f"{ANSI_BOLD}TLDR:{ANSI_RESET} "
    prompt += "\n"

    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0,
        prompt_context=["computer-related"]
    )
    answer = completion.choices[0].text.strip()
    return answer

if __name__ == '__main__':
    generate_answer()
