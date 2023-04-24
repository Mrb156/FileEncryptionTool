# Use an official Python runtime as a parent image
FROM ubuntu:latest
FROM python:3.10-slim-buster
RUN apt-get update
# # Set the working directory to /app
WORKDIR /src
# # Copy the current directory contents into the container at /app
COPY src/ /src

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install evdev
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip install flask

CMD [ "python", "./src/server.py" ]
