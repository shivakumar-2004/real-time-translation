# Real-Time Language Translation Using NMT

## Overview

This project is a real-time language translation system using Neural Machine Translation (NMT). It leverages pre-trained MarianMT models from Helsinki-NLP and provides an easy-to-use interface for translating text between multiple languages. The backend is built with FastAPI, while Streamlit serves as the frontend.

## Features

- Real-time text translation between multiple languages
- FastAPI-based backend for handling API requests
- Streamlit-powered frontend for an interactive user interface
- Uses Helsinki-NLP MarianMT pre-trained models
- Supports multiple concurrent translation requests

## Technologies Used

- **FastAPI**: Backend API for handling translation requests
- **Streamlit**: Frontend UI for user interaction
- **Transformers (Hugging Face)**: MarianMT models for translation
- **Torch**: Required for running the translation models
- **Requests**: For making API calls from the frontend

## Installation

### Prerequisites

Ensure you have Python 3.8 or later installed.

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI backend:
   ```bash
   uvicorn translator:app --reload
   ```
4. Run the Streamlit frontend:
   ```bash
   streamlit run app2.py
   ```

## Usage

1. Open the Streamlit UI in your browser.
2. Select the source and target languages.
3. Enter text and click **Translate**.
4. View the translated output instantly.

## API Endpoint

- **POST /translate/**
  - Request Body:
    ```json
    {
      "source_lang": "en",
      "target_lang": "fr",
      "text": "Hello, how are you?"
    }
    ```
  - Response:
    ```json
    {
      "translated_text": "Bonjour, comment allez-vous?"
    }
    ```

## Contributing

Feel free to submit pull requests for improvements or additional features.

## License

This project is licensed under the MIT License.

## Contact

For any queries, reach out via GitHub Issues.

