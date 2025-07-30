#!/bin/bash

# sed -i "$DATABASE" "s/-/$DATABASE/" .env
uvicorn run:app --host 0.0.0.0 --port $BACKEND_PORT
