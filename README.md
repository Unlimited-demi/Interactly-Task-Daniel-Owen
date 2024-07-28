# Profile Matching System

## Overview

The Profile Matching System is designed to match candidate profiles with job descriptions using advanced machine learning techniques. The system leverages MongoDB for database management, Elasticsearch for indexing, and a fine-tuned Language Model (LLM) for profile matching. It features a Flask backend and a React frontend, providing an intuitive and user-friendly interface.

## Project Structure

```
Profile_matching
├── README.md
├── requirements.txt
├── Dockerfile
├── package-lock.json
├── .git
├── data
│   ├── candidate_data.csv
│   ├── resume.csv
├── database
│   ├── setup_mongodb.py
│   ├── setup_elasticsearch.py
├── preprocessing
│   ├── preprocess.py
│   ├── index_mongodb.py
├── llm
│   ├── fine_tune.py
│   ├── generate_profiles.py
│   ├── rag.py
├── backend
│   ├── app.py
├── frontend
│   ├── public
│   │   ├── index.html
│   │   ├── styles.css
│   ├── src
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── components
│   │       ├── JobDescriptionInput.js
│   │       ├── ProfileDisplay.js
├── scripts
│   ├── cli.py
│   ├── run.sh
└── templates
    ├── index.html
```

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Node.js
- MongoDB
- Elasticsearch
- Docker (optional, for containerized setup)

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd Profile_matching
   ```

2. **Install backend dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies:**
   ```sh
   cd frontend
   npm install
   cd ..
   ```

4. **Setup MongoDB and Elasticsearch:**
   ```sh
   python database/setup_mongodb.py
   python database/setup_elasticsearch.py
   ```

### Running the Application

1. **Start the backend server:**
   ```sh
   python backend/app.py
   ```

2. **Start the frontend server:**
   ```sh
   cd frontend
   npm start
   cd ..
   ```

3. **Open your browser and navigate to:**
   ```
   http://localhost:3000
   ```

### Using Docker

1. **Build the Docker image:**
   ```sh
   docker build -t profile-matching .
   ```

2. **Run the Docker container:**
   ```sh
   docker run -p 5000:5000 profile-matching
   ```

3. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## CLI Usage

The project includes a command-line interface (CLI) for managing various tasks.

1. **View CLI help:**
   ```sh
   python scripts/cli.py --help
   ```

2. **Example CLI command:**
   ```sh
   python scripts/cli.py preprocess --input data/candidate_data.csv
   ```

## File Descriptions

- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `setup_mongodb.py`: Script to set up MongoDB.
- `setup_elasticsearch.py`: Script to set up Elasticsearch.
- `preprocess.py`: Script to preprocess the data.
- `index_mongodb.py`: Script to index data in MongoDB.
- `fine_tune.py`: Script to fine-tune the language model.
- `generate_profiles.py`: Script to generate candidate profiles.
- `rag.py`: Script for RAG (retrieval-augmented generation) implementation.
- `app.py`: Main Flask application.
- `cli.py`: Command-line interface script.
- `run.sh`: Shell script to run the application.
- `index.html`: Main HTML template.
- `styles.css`: Main CSS styles.
- `App.js`, `index.js`, `JobDescriptionInput.js`, `ProfileDisplay.js`: React components for the frontend.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License.

