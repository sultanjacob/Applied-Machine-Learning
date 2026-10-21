# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies first (caches this layer to speed up future builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the neural network models and the FastAPI script
COPY models/ ./models/
COPY app.py .

# Expose port 8001 for the Streamlit dashboard to connect to
EXPOSE 8001

# Launch the FastAPI server
CMD ["uvicorn", "app:app_full", "--host", "0.0.0.0", "--port", "8001"]
