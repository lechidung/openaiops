FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements files
COPY ai_models/requirements.txt ./ai_models/requirements.txt
COPY log_ingestion/requirements.txt ./log_ingestion/requirements.txt
COPY alerting/requirements.txt ./alerting/requirements.txt
COPY dashboard/requirements.txt ./dashboard/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r ai_models/requirements.txt
RUN pip install --no-cache-dir -r log_ingestion/requirements.txt
RUN pip install --no-cache-dir -r alerting/requirements.txt
RUN pip install --no-cache-dir -r dashboard/requirements.txt

# Copy the application code
COPY . .

# Expose the port for the dashboard
EXPOSE 5000

# Command to run the dashboard application
CMD ["python", "dashboard/app.py"]