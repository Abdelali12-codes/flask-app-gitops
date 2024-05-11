FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

ENTRYPOINT gunicorn --bind 0.0.0.0:5000 main:app