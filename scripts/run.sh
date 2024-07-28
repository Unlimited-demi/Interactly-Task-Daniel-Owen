#!/bin/bash
echo "Setting up database..."
python database/setup_mongodb.py

echo "Preprocessing data..."
python preprocessing/preprocess.py

echo "Indexing data..."
python preprocessing/index_mongodb.py

echo "Fine-tuning LLM..."
python llm/fine_tune.py

echo "Starting backend server..."
python backend/app.py &

echo "Starting frontend server..."
cd frontend
npm start
