# NanoTemper Tech Challenge

This repo hosts my solution to NanoTemper tech challenge.

## Features

- FastAPI server with two routes - / and /findmax/
- Server may be used alone since it also has a minalist frontend in the home route
- Minimal client showing an example of the findmax api usage
- Unit tests for all the possible status code emitted by the server

## Tech

Technologies and packages used:

- Python3.10.7
- FastAPI latest
- Uvicorn latest
- Python-multipart latest
- Pandas latest
- Requests latest
- Httpx latest
- Pytest latest

Unfortunately, I had some problems trying to dockerize the application and due to time limitations, I did not fix versions for the packages. It would be for sure my next step when working again in this code.

## Installation

Steps to start and test the code:

```sh
git clone https://github.com/carneiroDotDev/FastApi-Tech-Challenge.git
cd FastApi-Tech-Challenge
python3 -m venv NanoTemper
source venv NanoTemper
pip3 install -r requirements.txt
uvicorn server.main:app --reload
```

That should be sufficient to make server frontend available when visiting

```
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
```

_Once the server is running_, the minimal client can be executed with:

```sh
python3 client/main.py
```

## Final comments:

Thanks for the challenge. It was my very first experience writing Python within the FastAPI and the developer experience was excelente.

As next step, I would:

- Dockerize the app
- Fix the package versions
- Develop one more route to export a png with the overplot of the max points over the distribution plot.
