FROM python:3.8

# ENV config:
ARG BOT_ENV

ENV BOT_ENV=${BOT_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  TELEGRAM_API_TOKEN="5449083361:AAGyNUlZZssw1NraEIggf1dP0m9R-89lGzQ" \
  TELEGRAM_ACCESS_ID="" \
  TELEGRAM_PROXY_URL="" \
  TELEGRAM_PROXY_LOGIN="" \
  TELEGRAM_PROXY_PASSWORD="" \
  TZ=Europe/Kyiv

# Set time-zone info:
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# System deps:
RUN pip install -U pip aiogram pytz poetry && apt-get update && apt-get install sqlite3

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$BOT_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code
COPY *.py ./
COPY createdb.sql ./

ENTRYPOINT ["python", "app.py"]