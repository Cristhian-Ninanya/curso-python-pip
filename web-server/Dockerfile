FROM python:3.10

WORKDIR /web-server
COPY requeriments.txt /web-server/requeriments.txt

RUN pip3 install --no-cache-dir --upgrade -r /web-server/requeriments.txt

COPY . /web-server/

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]