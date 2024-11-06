#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Define some environment variables
export IMAGE_NAME="simple-translate-gemini"
export BASE_DIR=$(pwd)
export SECRETS_DIR=$(pwd)/../secrets/
export GOOGLE_APPLICATION_CREDENTIALS="/secrets/mega-pipeline.json"

# Build the image based on the Dockerfile
#docker build -t $IMAGE_NAME -f Dockerfile .
docker build -t $IMAGE_NAME --platform=linux/amd64 -f Dockerfile .

# Run the container
#docker run --rm --name $IMAGE_NAME -ti $IMAGE_NAME
docker run --rm --name $IMAGE_NAME -ti \
-v "$BASE_DIR":/app \
-v "$SECRETS_DIR":/secrets \
-e GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS \
$IMAGE_NAME



# docker tag simple-translate-gemini dlops/simple-translate-gemini
# docker push dlops/simple-translate-gemini