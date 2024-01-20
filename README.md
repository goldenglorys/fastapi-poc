# Delivery Fee Calculator API

## Description

A single endpoint API that calculates the delivery fee based on the information in the request payload (JSON) 
and includes the calculated delivery fee in the response payload (JSON). It is built using Python, FastAPI, and Pydantic as the data validation tool.

### Tech Stack Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Pydantic](https://img.shields.io/badge/pydantic-%23e92063.svg?style=for-the-badge&logo=pydantic&logoColor=white)
![Poetry](https://img.shields.io/badge/poetry-%230db7ed.svg?style=for-the-badge&logo=poetry&logoColor=white)

### Dependencies
The API has been dockerized and will require docker desktop to run successfully.
* Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Running API
* Make sure the docker daemon is running.
* Make sure you are in the root directory of the project. The root directory contains the Dockerfile.

* Run the docker compose command below in the project root directory to start the application.

```
docker compose up --build
```

### Testing

You can either test the api with FastAPI docs:

[![Docs](https://img.shields.io/badge/Fast_API-/docs-0088CC?style=for-the-badge&logo=fastAPI&logoColor=#419dda)](http://127.0.0.1:8000/docs)

sample request:
```
{
    "cart_value": 790,
    "delivery_distance": 2235,
    "amount_of_items": 4,
    "time": "2024-01-15T13:00:00Z"
}
```
Output:
```
{"delivery_fee":710}
```

## **Pytest**

Alternatively you can use the tests in test_fees.py by running "pytest" command in the project folder.

```
pytest
```
---