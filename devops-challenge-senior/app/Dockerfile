FROM python:3.11-slim

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

# Copy files before switching to non-root user
COPY requirements.txt .
COPY app.py .

# Install dependencies as root
RUN pip install --no-cache-dir -r requirements.txt

# Change ownership of files to non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
