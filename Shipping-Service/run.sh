#!/usr/bin/env bash

python src/rest_service.py &
python src/grpc_service.py &

while true; do
    # echo "running"
    sleep 1  # Adjust the sleep duration as needed
done