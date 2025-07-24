# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install gcc
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download ca_core_news_sm

# Copy the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "rspacy.api:app", "--host", "0.0.0.0", "--port", "8000"]
