# BASE
FROM python:3.10-buster

ENV \
    # python:
    PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/pybay-venv \
    # poetry:
    POETRY_VERSION=1.5.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# install poetry
RUN pip install "poetry==$POETRY_VERSION"

# copy requirements
COPY pyproject.toml poetry.lock ./

# add venv to path 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python packages
RUN python -m venv $VIRTUAL_ENV \
	&& . $VIRTUAL_ENV/bin/activate \
	&& poetry install --no-root

WORKDIR /code

COPY app /code/app/