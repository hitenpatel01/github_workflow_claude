"""CLI entry point for GitHub Workflow Claude."""

import click
from rich.console import Console

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


if __name__ == "__main__":
    main()
