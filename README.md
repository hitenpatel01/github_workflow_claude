# GitHub Workflow Claude

GitHub API automation tool powered by Claude.

## Setup

1. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e ".[dev]"
   ```

3. Create a `.env` file with your credentials:
   ```
   GITHUB_TOKEN=your_github_token_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

## Development

### Running the CLI
```bash
ghw --help
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/test_github.py

# Run in watch mode (requires pytest-watch)
pytest-watch
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/
```

## Project Structure

```
src/github_workflow_claude/
  ├── __init__.py
  ├── cli.py              # CLI entry point
  ├── github/             # GitHub API interactions
  │   ├── __init__.py
  │   └── client.py
  ├── claude/             # Claude AI integration
  │   ├── __init__.py
  │   └── client.py
  └── workflows/          # Workflow automation logic
      ├── __init__.py
      └── handlers.py

tests/
  ├── __init__.py
  ├── test_github.py
  └── test_claude.py
```

## License

MIT
