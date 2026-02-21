"""Tests for GitHub client."""

import pytest
from github_workflow_claude.github.client import GitHubClient


def test_github_client_requires_token() -> None:
    """Test that GitHubClient raises error without token."""
    with pytest.raises(ValueError, match="GitHub token is required"):
        GitHubClient(token=None)
