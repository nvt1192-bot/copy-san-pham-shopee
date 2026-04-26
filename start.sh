#!/bin/bash
cd backend

pip3 install fastapi uvicorn openai playwright supabase
playwright install

python3 -m uvicorn main:app --host 127.0.0.1 --port 8000
