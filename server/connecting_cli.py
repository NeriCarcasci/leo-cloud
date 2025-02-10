import click
import logging
from prompt_generator import generate_prompt
from ai_command_generator import get_ai_generated_command
from commands_execute import execute_command  # Ensure safe execution

# Setup logging for debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("cli_app.log"),  # Save logs to a file
        logging.StreamHandler()  # Display logs in the console
    ]
)

@click.command()
@click.argument("query", type=str, required=True)
def run(query):
    """
    Converts user input into an AI-generated shell command and executes it.

    Example Usage:
    python cli.py "List all active Docker containers"
    """
    logging.info(f"Received user query: {query}")

    # Generate structured prompt for AI
    prompt = generate_prompt(query)
    logging.info(f"Generated AI prompt: {prompt}")

    # Request AI-generated command
    ai_command = get_ai_generated_command(prompt)

    if not ai_command:
        click.secho("AI did not generate a valid command.", fg="yellow")
        return

    # Confirm execution for safety
    click.secho(f"AI Generated Command: {ai_command}", fg="green")
    confirm = click.confirm("Do you want to execute this command?", default=False)

    if confirm:
        logging.info(f"Executing command: {ai_command}")
        execute_command(ai_command)
    else:
        click.secho("Command execution canceled.", fg="red")


# Define CLI entry point
@click.group()
def cli():
    """AI-powered CLI for generating and executing shell commands."""
    pass


# Register the command in CLI
cli.add_command(run)

if __name__ == "__main__":
    cli()
