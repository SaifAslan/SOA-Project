FROM python:3.10.5-alpine3.16
COPY . /app
WORKDIR /app/api
RUN pip install -r ../requirements.txt
CMD python -m flask run --port=6000 --host=0.0.0.0