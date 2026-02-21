"""GitHub API client."""

from typing import Optional
from github import Github
import os


class GitHubClient:
    """Client for interacting with GitHub API."""

    def __init__(self, token: Optional[str] = None) -> None:
        """Initialize GitHub client.

        Args:
            token: GitHub personal access token. If None, reads from GITHUB_TOKEN env var.
        """
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GitHub token is required")

        self.client = Github(self.token)

    def get_user(self) -> str:
        """Get the authenticated user's login.

        Returns:
            The authenticated user's GitHub login.
        """
        return self.client.get_user().login
