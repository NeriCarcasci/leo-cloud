import subprocess
import logging
import shlex
from rich.console import Console

console = Console()

def execute_command(command: str):
    """
    Safely executes the AI-generated shell command.
    
    Args:
        command (str): The shell command to execute.

    Returns:
        None
    """
    logging.info(f"Executing command: {command}")

    try:
        # Use shlex to safely parse the command
        cmd_parts = shlex.split(command)

        # Execute command using subprocess (prevents shell injection)
        result = subprocess.run(cmd_parts, capture_output=True, text=True, check=True)

        # Display output
        console.print(f"[green]Command Output:[/green]\n{result.stdout}")
    
    except subprocess.CalledProcessError as CPE:
        console.print(f"[red]Command failed:[/red] {CPE.stderr}")
        logging.error(f"Command execution failed: {CPE.stderr}")

    except Exception as E:
        console.print(f"🚨 [red]Unexpected error while executing command:[/red] {str(E)}")
        logging.exception("Unexpected error occurred.")
