FROM python:3.8-alpine
RUN apk add --no-cache bash

EXPOSE 9888

RUN apk add build-base unixodbc-dev unixodbc freetds-dev && pip install pyodbc

#ADD odbcinst.ini /odbcinst.ini
#RUN apt-get update
#RUN apt-get install -y tdsodbc unixodbc-dev
#RUN apt install unixodbc-bin -y
#RUN apt-get clean -y

WORKDIR /telegram-sync

COPY requirements.txt /telegram-sync

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY run.sh /
RUN chmod +x /run.sh

CMD ["./wait-for-it.sh", "rabbitmq:5672", "--", "/bin/sh", "./run.sh"]

#COPY ./docker-entrypoint.sh /docker-entrypoint.sh
#RUN chmod +x /docker-entrypoint.sh
#ENTRYPOINT ["/bin/sh", "./docker-entrypoint.sh"]