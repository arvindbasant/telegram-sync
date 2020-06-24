FROM python:3.8-alpine

EXPOSE 52004

RUN apk add bash build-base unixodbc-dev unixodbc freetds-dev

WORKDIR /telegram-sync

COPY requirements.txt /telegram-sync

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY run.sh /
RUN chmod +x /run.sh

CMD /bin/sh -c './wait-for-it.sh -t 60 rabbitmq:5672 -- /bin/sh ./run.sh'
