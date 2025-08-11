# Sentiment Analyzer with FastAPI and Streamlit

This project is a local sentiment analysis web application built with a **FastAPI backend** and a **Streamlit frontend**.  
It uses the **Ollama Mistral** language model to analyze the sentiment of input text and return a detailed sentiment response.

---

## Features

- **FastAPI backend** exposing a `/analyze/` POST endpoint for sentiment analysis.
- **Streamlit frontend** for text input and displaying sentiment results.
- Integration with the **Ollama Mistral** model for advanced NLP sentiment classification.
- Interactive API documentation via FastAPI’s Swagger UI at `/docs`.

---

## Project Structure

sentiment-analyzer-mistral/
│
├── backend/
│ ├── main.py # FastAPI backend code with /analyze/ API
│
├── frontend/
│ ├── app.py # Streamlit frontend app
│
└── README.md


---

## Prerequisites

- Python 3.9+
- Ollama Mistral model installed and running
- Virtual environment (`venv`) recommended

---

## Setup Instructions

1. **Clone the repository**
git clone <your-repo-url>
cd sentiment-analyzer-mistral


2. **Create and activate a virtual environment**
python3 -m venv venv
source venv/bin/activate # macOS / Linux
.\venv\Scripts\activate # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Start the FastAPI backend**
uvicorn backend.main:app --reload --port 8001

Access API docs at: [http://localhost:8001/docs](http://localhost:8001/docs)

5. **Start the Streamlit frontend**
In a new terminal (with venv activated):
streamlit run frontend/app.py

Access frontend UI at: [http://localhost:8501](http://localhost:8501)

---

## Usage

1. Open the Streamlit app: [http://localhost:8501](http://localhost:8501)
2. Type any text in the input box.
3. Click **Analyze**.
4. The app sends your text to the backend `/analyze/` API.
5. The backend processes the text via Ollama Mistral and returns sentiment.
6. The result is displayed in the Streamlit interface.

---

## API Endpoint

**POST** `/analyze/`  
Form data:
- `text` (string) — The text to analyze

Example cURL test:
curl -X POST -F "text=I love this app" http://localhost:8001/analyze/


---

## Troubleshooting

- **404 Not Found on `/`** → Visit `/docs` to test API, or add a root route.
- **Streamlit connection error** → Start backend first, confirm it’s running on port 8001.
- **Both servers must run at the same time** — one terminal for FastAPI, another for Streamlit.
- Use consistent `localhost` / port values in frontend calls.

---

## Next Steps

- Return only "Positive", "Negative", or "Neutral" for cleaner output.
- Improve error handling in backend and frontend.
- Deploy to cloud or share with **ngrok** for public testing.
- Add authentication and logging.

---

## Contact

Author: **[Your Name]**  
Email: **[Your Email]**

---

**Enjoy analyzing sentiments with your new app!**


# Sentiment Analyzer App — Public Testing Info

Welcome! This is a local sentiment analysis app with a FastAPI backend and Streamlit frontend.

## How to Access the App

- **Frontend (Streamlit UI):**  
  Open in your browser:  
  `http://<YOUR_IP_OR_HOST>:8501`  

- **Backend API (FastAPI):**  
  For API docs and testing:  
  `http://<YOUR_IP_OR_HOST>:8001/docs`  

> Replace `<YOUR_IP_OR_HOST>` with the actual machine IP or hostname running the app.

---

## Important Notes for Testers

- The app consists of two parts running on different ports (`8501` for frontend UI, `8001` for backend API).
- The frontend UI (where you enter text and get sentiment) is at port 8501.
- The API docs (FastAPI Swagger UI) is accessible at port 8001.
- **Make sure both backend and frontend are running simultaneously**.

---

## Quick Usage Guide

1. Visit the frontend URL (`http://<YOUR_IP_OR_HOST>:8501`).
2. Enter the text you want to analyze.
3. Click the **Analyze** button.
4. View the sentiment result displayed instantly.

---

## Backend API Testing (Optional)

Send a POST request (e.g., via curl):
curl -X POST -F "text=I love this app!" http://<YOUR_IP_OR_HOST>:8001/analyze/


You will receive a JSON response showing the sentiment analysis.

---

## For Host

If you want to share this app over the internet, consider:

- Running the servers on `0.0.0.0` to allow network access.
- Using tools like **ngrok** to create a public URL forwarding traffic to your local machine.

---

Thank you for testing the Sentiment Analyzer app!  
Feel free to reach out if you have questions.

---

*This README is intended for public testers of the app.*

