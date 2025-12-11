# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY agent.py .
COPY langgraph.json .
COPY .env .

# Expose port 8000
EXPOSE 8000

# Run LangGraph API
CMD ["langgraph", "api", "server"]