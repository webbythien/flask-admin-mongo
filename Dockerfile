# Base Image
FROM python:3.10.13-alpine3.17

WORKDIR /admin

# Copy and install dependencies
COPY . .
RUN pip install -r requirements.txt

# Copy the rest of the application files
# COPY . .

# Expose the necessary port
EXPOSE 5009

# Run the server
CMD ["python", "app.py"]
