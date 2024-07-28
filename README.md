# Interactly Task - Profile Matching System

## Overview
This project aims to develop a profile matching system that matches candidate profiles based on job descriptions.

## Setup
1. Install the dependencies: `pip install -r requirements.txt`
2. Setup the database: `python database/setup_mongodb.py`
3. Preprocess and index data: `python preprocessing/preprocess.py` and `python preprocessing/index_mongodb.py`
4. Fine-tune the LLM: `python llm/fine_tune.py`
5. Start the backend server: `python backend/app.py`
6. Start the frontend server: `npm start` inside the `frontend` directory

## Usage
- Use the chat interface to enter job descriptions and retrieve matching candidate profiles.
