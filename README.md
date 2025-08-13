
# mcp-wait: Model Context Protocol (MCP) Server

mcp-wait is a reference [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that demonstrates a simple note storage system and a wait utility, built using the [create-python-server SDK](https://github.com/modelcontextprotocol/create-python-server).

## Features

- **Tools:**
  - `wait`: Wait for a specified number of seconds before responding
    - Argument: `seconds` (integer)

## Quickstart

### Prerequisites
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- Python 3.8+

### Installation

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Run the server:**
   ```bash
   uv --directory . run wait
   ```

### Claude Desktop Integration

Add the following to your Claude Desktop config:

**Development/Unpublished:**
```json
"mcpServers": {
  "wait": {
    "command": "uv",
    "args": ["--directory", "C:/cnext/mcp-wait", "run", "wait"]
  }
}
```

**Published:**
```json
"mcpServers": {
  "wait": {
    "command": "uvx",
    "args": ["wait"]
  }
}
```

## Development

### Build & Publish
1. Sync dependencies:
   ```bash
   uv sync
   ```
2. Build distributions:
   ```bash
   uv build
   ```
3. Publish to PyPI:
   ```bash
   uv publish
   ```
   - Set credentials via `--token`/`UV_PUBLISH_TOKEN` or `--username`/`UV_PUBLISH_USERNAME` and `--password`/`UV_PUBLISH_PASSWORD`

### Debugging
For best results, use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):
```bash
npx @modelcontextprotocol/inspector uv --directory C:/cnext/mcp-wait run wait
```
Open the displayed URL in your browser to debug.

## Containerization

Build and run with Docker:
```bash
docker build -t mcp-wait .
docker run --rm -p 8000:8000 mcp-wait
```

## Project Structure

- `src/wait/` — Main server implementation
- `Dockerfile` — Containerization
- `pyproject.toml` — Project metadata and dependencies
- `uv.lock` — Dependency lockfile