FROM python:3.12-slim

WORKDIR /app

COPY . .

# Remove any local venv to avoid uv using it
RUN rm -rf .venv

ENV PYTHONPATH=/app/src

# Install ODBC Driver 18 for SQL Server and dependencies
RUN apt-get update \
    && apt-get install -y curl gnupg2 apt-transport-https ca-certificates \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-prod.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install mcp, uv, and project dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && UV_VIRTUALENV_CREATE=0 uv sync --dev --all-extras

EXPOSE 8000

CMD ["python", "-m", "mpl_mcp.server"]
