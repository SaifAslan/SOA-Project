
FROM python:3-slim-buster

RUN mkdir /src

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 50051

COPY . .

CMD ["bash", "run.sh"]