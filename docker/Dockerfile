FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/code
RUN mkdir /opt/requirements
WORKDIR /opt/code

COPY requirements.txt /opt/requirements/requirements.txt
RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    pip install -r /opt/requirements/requirements.txt

CMD [ "python", "wsgi.py" ]
