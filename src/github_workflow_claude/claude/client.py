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

    def summarize_text(self, text: str, max_words: int = 100) -> str:
        """Summarize the given text using Claude.

        Args:
            text: The text to summarize.
            max_words: Maximum number of words in the summary.

        Returns:
            A summarized version of the text.
        """
        prompt = f"Summarize the following text in {max_words} words:\n\n{text}"
        response = self.generate_response(prompt)
        words = response.split(" ")
        return " ".join(words[:max_words - 1])
