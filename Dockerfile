# Pull official base image
FROM python:3.9-slim-buster

# Set work directory
WORKDIR /app

# Set enviroment variables
ENV DATABASE_URL default

# Install pip requirements
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN python -m pip install -r requirements.txt

# Copy Project
COPY . /app

# Expose port
EXPOSE 5000

#Run app
CMD ["python3", "application.py"]