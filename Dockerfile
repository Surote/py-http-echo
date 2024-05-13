FROM registry.access.redhat.com/ubi9/python-311:1-62

WORKDIR /py-http-echo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates ./templates/
COPY app.py .

CMD [ "gunicorn", "-b", "0.0.0.0:8080", "app:app"]