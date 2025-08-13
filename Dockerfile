# Dockerfile for MCP Wait Server
FROM python:3.12-slim

WORKDIR /app

COPY . .

# Remove any local venv to avoid uv using it
RUN rm -rf .venv

ENV PYTHONPATH=/app/src

# Install mcp, uv, fastapi, and uvicorn and project dependencies
RUN pip install --upgrade pip \
    && pip install fastmcp uv \
    && UV_VIRTUALENV_CREATE=0 uv sync --dev --all-extras

EXPOSE 8000

CMD ["python", "-m", "wait.server", "--http"]
