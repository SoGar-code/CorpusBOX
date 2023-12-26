###########
# BUILDER #
###########
FROM python:3.10-slim as builder

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install packages
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y gcc python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt .
RUN python -m pip wheel --no-cache-dir --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########
FROM python:3.10-slim

COPY --from=builder /usr/src/app/wheels /wheels/
RUN apt-get update && apt-get install -y gcc python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --no-cache /wheels/*

#Opened ports: jupyter
EXPOSE 5000

ENV PYTHONPATH=/app

CMD jupyter lab --no-browser --ip 0.0.0.0 --allow-root --port 5000
