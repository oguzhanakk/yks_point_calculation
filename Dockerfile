FROM python:3.9
# actually python image is debian based

ENV DEBIAN_FRONTEND noninteractive

RUN pip install --upgrade pip

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app