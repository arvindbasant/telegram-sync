FROM python:3.8

ADD odbcinst.ini /odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

WORKDIR /telegram-sync

COPY requirements.txt /telegram-sync

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY run.sh /
RUN chmod +x /run.sh

CMD ["/bin/bash", "./run.sh"]

#CMD ["python3", "stream_handlers.telegram_provider & stream_handlers.telegram_consumer"]