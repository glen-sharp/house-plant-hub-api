# Use an official Python runtime as the base image
FROM python:3.9
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Run DB creation and load scripts
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose port 8000 for the development server to listen on
EXPOSE 8000
# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]