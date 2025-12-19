#!/bin/bash

echo "Starting Spike AI Analytics & SEO Agent..."

# Create virtual environment if not exists
if [ ! -d ".venv" ]; then
  python -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Load environment variables
export $(grep -v '^#' .env | xargs)

# Start server
uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT:-8080}
