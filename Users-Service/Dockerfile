# FROM python:3.10.5-alpine3.16
# COPY . /app
# WORKDIR /app/api
# RUN pip install -r ../requirements.txt
# CMD python -m flask run --port=7000 --host=0.0.0.0

FROM python:3.10.5-alpine3.16
COPY . /app
WORKDIR /app/api
RUN pip install -r ../requirements.txt
CMD python -m flask run --port=6001 --host=0.0.0.0