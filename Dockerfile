FROM python:3.9-slim-buster

WORKDIR /py-http-echo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .

CMD [ "python3", "app.py"]