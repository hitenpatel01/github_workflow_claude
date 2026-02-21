"""Tests for Claude client."""

import pytest
from github_workflow_claude.claude.client import ClaudeClient


def test_claude_client_requires_api_key() -> None:
    """Test that ClaudeClient raises error without API key."""
    with pytest.raises(ValueError, match="Anthropic API key is required"):
        ClaudeClient(api_key=None)
