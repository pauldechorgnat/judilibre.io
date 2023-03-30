FROM python:3.10-slim-buster

ADD requirements.txt /

RUN python -m pip install -r /requirements.txt

ADD static /static
ADD templates /templates
ADD app.py /app.py

WORKDIR /

EXPOSE 5000

CMD [ "python", "app.py"]