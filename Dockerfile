FROM registry.access.redhat.com/ubi9/python-311:1-77

WORKDIR /py-http-echo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates ./templates/
COPY certificate ./certificate
COPY app.py .

#CMD [ "gunicorn", "-b", "0.0.0.0:8080", "app:app"]
CMD [ "gunicorn", "-b", "0.0.0.0:8443", "app:app","--certfile=/py-http-echo/certificate/tls.crt", "--keyfile=/py-http-echo/certificate/tls.key"]