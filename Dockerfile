# Use the official python image for python3 - using Debian because idk.
FROM python:3-stretch

# Will be listening on port 8000
EXPOSE 8000

# Create working directory
WORKDIR /ists

# Install packages required to build uWSGI
RUN apt-get update -y
RUN apt-get install -y \
    build-essential \
    python-dev

# Install pip requirements
COPY requrements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Configure uWSGI
COPY uwsgi.ini ./uwsgi.ini

# Run the application on startup
CMD uwsgi --ini uwsgi.ini

# Set flask app
ENV FLASK_APP project

# Copy over application files
COPY project ./project

# Configure application
COPY config.py ./instance/config.py

# Add website posts
COPY ./posts ./instance/posts
