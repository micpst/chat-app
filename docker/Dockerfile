FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code

ENTRYPOINT [ "python" ]

CMD [ "wsgi.py" ]
