FROM python:3.6-slim-stretch

RUN pip install pandas sklearn

RUN mkdir /app
COPY launcher.py /app
COPY mmlibrary.py /app
COPY mymodel.py /app
COPY binary.zip /app

WORKDIR /app

ENTRYPOINT ["python3", "-u", "launcher.py"]
