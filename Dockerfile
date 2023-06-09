# Use the official Python base image
FROM python:slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory to the container
COPY . .

# Expose the port on which the Flask app will run (default is 5000)
EXPOSE 5000

# Set the environment variables if needed
# ENV VARIABLE_NAME value

# Start the Flask app
CMD ["python", "main.py"]
