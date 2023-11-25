#!/bin/sh

alembic upgrade head

python server.py