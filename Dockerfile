# app/Dockerfile

FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY app /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 8502
ENTRYPOINT ["python","-m","streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0"]