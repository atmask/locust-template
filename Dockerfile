FROM python:3.9-slim

WORKDIR /LoadTests
COPY . /LoadTests

RUN pip install poetry && \
    poetry install &&

ENTRYPOINT ["/LoadTests/.venv/bin/locust", "AppUser"]