import platform
import subprocess
from rich.console import Console

console = Console()

def get_user_environment():
    """
    Retrieves the user's operating system, shell, and installed tools.
    
    Returns:
        dict: A dictionary containing OS, shell, and a list of installed tools.
    """
    user_os = platform.system()
    user_shell = subprocess.run("echo $SHELL", shell=True, capture_output=True, text=True).stdout.strip()
    installed_tools = subprocess.run("compgen -c", shell=True, capture_output=True, text=True).stdout.strip().split("\n")

    return {
        "user_os": user_os,
        "user_shell": user_shell,
        "installed_tools": installed_tools[:12]  # Limiting to first 12 tools for readability
    }

def generate_prompt(user_request):
    """
    Generates a structured prompt based on the user's request and system context.

    Args:
        user_request (str): The command or request from the user.

    Returns:
        str: A formatted prompt string.
    """
    environment_data = get_user_environment()
    
    if not environment_data:
        return None  # Stop if environment retrieval fails

    expected_output = "[Generated Linux command]"  # Define expected output placeholder

    # Construct the AI prompt using f-strings for better readability
    prompt_template_for_user = f"""
# Generate a Linux command based on user input like 'make x y z'
# User input:

"{user_request}"

# System context:
- Operating System: {environment_data["user_os"]}
- Shell: {environment_data["user_shell"]}
- Installed Tools: {', '.join(environment_data["installed_tools"])}

# Constraints:
- The output must be a single valid shell command.
- The command should be optimized for efficiency (e.g., creating an alias should be done correctly, without excessive redirection).
- Avoid destructive commands like 'rm'.

# Expected Output:
"{expected_output}"
    """

    console.print(f"[yellow]Generated AI prompt:[/yellow]\n{prompt_template_for_user}")
    return prompt_template_for_user

# Example usage:
if __name__ == "__main__":
    user_request = input("Enter your command request: ")
    generate_prompt(user_request)


  
