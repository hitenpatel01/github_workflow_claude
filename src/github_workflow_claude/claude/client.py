"""Claude AI client."""

from typing import Optional
import os
from anthropic import Anthropic


class ClaudeClient:
    """Client for interacting with Claude AI."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Initialize Claude client.

        Args:
            api_key: Anthropic API key. If None, reads from ANTHROPIC_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Anthropic API key is required")

        self.client = Anthropic(api_key=self.api_key)

    def generate_response(self, prompt: str, model: str = "claude-sonnet-4-5-20250929") -> str:
        """Generate a response from Claude.

        Args:
            prompt: The prompt to send to Claude.
            model: The model to use (default: claude-sonnet-4-5-20250929).

        Returns:
            Claude's response text.
        """
        message = self.client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
