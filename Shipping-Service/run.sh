#!/usr/bin/env bash
python src/grpc_service.py &
python src/rest_service.py &