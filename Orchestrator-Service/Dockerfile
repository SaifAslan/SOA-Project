
FROM python:3-slim-buster

RUN mkdir /src

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 6000

COPY . .
COPY src/carts.wsdl .

CMD ["python", "src/app.py"]