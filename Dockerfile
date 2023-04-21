FROM ubuntu
# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

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

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
# ENV NAME World

# Run when the container launches
# ENTRYPOINT ["python", "zipper.py"]

# FROM ubuntu:latest

# COPY src/* /src
# WORKDIR /src

# RUN apt-get update && \
#     apt-get install -y gcc build-essential && \
#     apt-get install -y python3 python3-pip python3-dev build-essential && \
#     rm -rf /var/lib/apt/lists/*

# RUN pip3 install evdev

# RUN pip install -r requirements.txt

CMD ["/bin/bash"]
