FROM python:3

ENV PYTHONUNBUFFERED 1

COPY runner.py /src/runner.py

CMD ['/bin/sh']