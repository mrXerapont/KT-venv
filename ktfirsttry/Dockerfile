FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ktfirsttry
WORKDIR /ktfirsttry
COPY requirements.txt /ktfirsttry/
RUN pip install -r requirements.txt
COPY . /ktfirsttry/
