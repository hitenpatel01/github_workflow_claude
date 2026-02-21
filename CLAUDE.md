# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

GitHub API automation tool powered by Claude AI. This is a Python application that uses the GitHub API to automate workflows and Claude AI for intelligent decision-making.

## Development Setup

This project uses **uv** for package management. Always work within the virtual environment:

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies (including dev dependencies)
uv pip install -e ".[dev]"

# Sync dependencies from pyproject.toml
uv pip sync
```

## Common Commands

### Testing
- `pytest` - Run all tests
- `pytest tests/test_github.py` - Run specific test file
- `pytest -v --cov` - Run with verbose output and coverage
- `pytest -k test_name` - Run tests matching pattern

### Code Quality
- `black src/ tests/` - Format code (100 char line length)
- `ruff check src/ tests/` - Lint code
- `ruff check --fix src/ tests/` - Auto-fix linting issues
- `mypy src/` - Type checking

### Running the Application
- `ghw --help` - CLI help
- `python -m github_workflow_claude.cli` - Alternative way to run CLI

## Architecture

### Module Structure

The codebase is organized into three main modules under `src/github_workflow_claude/`:

1. **`github/`** - GitHub API interactions
   - Uses PyGithub library for GitHub API calls
   - `client.py` contains the GitHubClient wrapper
   - Requires GITHUB_TOKEN environment variable

2. **`claude/`** - Claude AI integration
   - Uses Anthropic Python SDK
   - `client.py` contains the ClaudeClient wrapper
   - Requires ANTHROPIC_API_KEY environment variable
   - Defaults to claude-sonnet-4-5-20250929 model

3. **`workflows/`** - Automation logic
   - Combines GitHub and Claude clients to automate tasks
   - Currently a placeholder for future workflow implementations

4. **`cli.py`** - Command-line interface
   - Built with Click framework
   - Uses Rich for terminal output
   - Entry point defined in pyproject.toml as `ghw` command

### Configuration

- Environment variables loaded from `.env` file (use `.env.example` as template)
- All configuration in `pyproject.toml` (dependencies, tools, scripts)
- Type hints required on all functions (enforced by mypy)

### Testing

- Tests live in `tests/` directory
- Use pytest for testing framework
- Coverage reporting configured to track `src/github_workflow_claude/`
- Mock external API calls in tests (GitHub API, Anthropic API)
