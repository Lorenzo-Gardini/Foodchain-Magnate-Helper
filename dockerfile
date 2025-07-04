FROM python:3.13-slim

RUN pip install uv

WORKDIR /app

# Copy only what’s needed first (better for Docker cache)
COPY pyproject.toml ./

RUN uv venv

RUN uv pip install .

# Copy rest of the app
COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
