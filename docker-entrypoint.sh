#!/usr/bin/env bash

echo "Waiting for MySQL..."

while ! nc -z db 3306; do
  sleep 0.5
done

echo "MySQL Started Successfully"

# Run migration and Start the server.
flask db upgrade
flask run
