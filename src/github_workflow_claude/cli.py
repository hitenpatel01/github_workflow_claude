"""CLI entry point for GitHub Workflow Claude."""

import click
from dotenv import load_dotenv
from rich.console import Console

from github_workflow_claude.claude.client import ClaudeClient

load_dotenv()

console = Console()


@click.group()
@click.version_option()
def main() -> None:
    """GitHub API automation powered by Claude."""
    pass


@main.command()
def status() -> None:
    """Check the status of the GitHub connection."""
    console.print("[green]GitHub Workflow Claude is ready![/green]")


@main.command()
@click.argument("prompt")
def ask(prompt: str) -> None:
    """Send a prompt to Claude and print the response."""
    try:
        client = ClaudeClient()
        response = client.generate_response(prompt)
        console.print(response)
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")


if __name__ == "__main__":
    main()
