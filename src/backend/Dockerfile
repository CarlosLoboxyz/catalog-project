FROM python:3.12-rc-alpine
ENV PYTHONBUFFERED 1
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .