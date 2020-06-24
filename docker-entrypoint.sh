#!/bin/bash

python3 -m stream_handlers.telegram_provider &
python3 -m stream_handlers.telegram_consumer