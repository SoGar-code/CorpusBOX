###########
# BUILDER #
###########
FROM python:3.10-slim as builder

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install packages
RUN python3 -m pip install --upgrade pip
COPY ./requirements.txt .
RUN python3 -m pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########
FROM python:3.10-slim

COPY --from=builder /usr/src/app/wheels /wheels
RUN python3 -m pip install --no-cache /wheels/*

#RUN apt-get update; apt-get install -y git

#Opened ports
#Jupyter
EXPOSE 5000
#Dash or Uvicorn
#EXPOSE 80

ENV PYTHONPATH=/app

CMD jupyter lab --no-browser --ip 0.0.0.0 --allow-root --port 5000