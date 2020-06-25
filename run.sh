#!/bin/bash

python3 -m jobs.rfid_response_prune &
python3 -m stream_handlers.telegram_provider &
python3 -m stream_handlers.telegram_consumer