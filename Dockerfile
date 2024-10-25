FROM registry.access.redhat.com/ubi9/python-311:1-77

WORKDIR /py-http-echo

USER root
RUN dnf -y upgrade

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY templates ./templates/
COPY app.py .

USER 1001
CMD [ "gunicorn", "-b", "0.0.0.0:8080", "app:app"]
#CMD [ "gunicorn", "-b", "0.0.0.0:8443", "app:app","--certfile=/py-http-echo/certificate/tls.crt", "--keyfile=/py-http-echo/certificate/tls.key"]