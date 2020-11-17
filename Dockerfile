FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Billy Jenkins billyjenkins417@gmail.com"

RUN pip install --no-cache-dir fastapi

COPY ./app /app