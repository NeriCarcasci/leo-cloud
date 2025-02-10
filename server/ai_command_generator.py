import openai
from dotenv import load_dotenv
import os
import logging
from rich.console import Console
from rich.traceback import install

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Enable Rich traceback for better error visualization
install()

console = Console()

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate API key at startup
if not OPENAI_API_KEY:
    console.print("[red]Missing OpenAI API key![/red] Please set it in `.env` file.")
    exit(1)  # Exit immediately if the key is missing


def get_ai_generated_command(prompt: str) -> str:
    """
    Sends a structured prompt to OpenAI's GPT model to generate a safe Linux shell command.
    
    Args:
        prompt (str): The user request to be processed by AI.
    
    Returns:
        str: The generated shell command, or None if an error occurs.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            api_key=OPENAI_API_KEY,  # Explicitly set API key
            messages=[
                {"role": "system", "content": "You are an AI that generates safe Linux shell commands."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50
        )

        # Extract AI-generated command
        command_output = response["choices"][0]["message"]["content"].strip()
        
        console.print(f"[green]Generated Command:[/green] {command_output}")
        return command_output

    except openai.error.OpenAIError as api_error:
        console.print(f"[red]OpenAI API Error:[/red] {api_error}")
        logging.error(f"OpenAI API Error: {api_error}")
    
    except Exception as e:
        console.print(f"[red]Unexpected Error:[/red] {str(e)}")
        logging.exception("Unexpected error occurred while generating command.")

    return None  # Return None if an error occurs


# Example usage
if __name__ == "__main__":
    user_input = "List all active Docker containers"
    get_ai_generated_command(user_input)

