#!/bin/bash

# Pull the latest changes from the Git repository
git pull origin main

# Build the Docker image and start the container
docker-compose up --build -d
