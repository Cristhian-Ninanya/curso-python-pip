FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"