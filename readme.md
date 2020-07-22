**Telegram Sync**

telegram_sync is a python service for parsing and storing EWM error Telegram to SQL SERVER.
It uses RabbitMQ as message broker to handle latency.
It also runs a schedule prune job to delete rfid_response older than 90 days.


**Running app locally for development**
    1. Create a docker network ts_net
    2. run sql server image with --net ts_net using command: docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Pass*123' -p 1433:1433 -d --net ts_net mcr.microsoft.com/mssql/server:latest