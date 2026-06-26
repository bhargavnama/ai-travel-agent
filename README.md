# 🌍 VoyageAI: Agentic Travel Orchestrator

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

**VoyageAI** is an advanced, autonomous AI travel planner built with an agentic workflow. Unlike standard chatbots, VoyageAI acts as an intelligent orchestrator—dynamically utilizing external tools and APIs to fetch real-time weather, currency exchange rates, and location data to generate highly accurate, premium travel itineraries.

This project demonstrates complex LLM orchestration, custom tool creation, and full-stack development, making it a robust showcase of modern AI engineering.

---

## ✨ Key Features
- **🧠 Agentic Workflow (LangGraph):** Employs a stateful, multi-step agent architecture that decides when and how to use external tools before formulating a response.
- **🛠️ Dynamic Tool Use:** 
  - **Weather Tool:** Fetches real-time climate data and multi-day forecasts for any destination via OpenWeatherMap.
  - **Currency Converter:** Provides live exchange rates via ExchangeRate-API.
  - **Places Search:** Uses Google Places API (with fallback support) to discover highly-rated hotels, restaurants, and attractions.
- **⚡ High-Performance Backend:** Built on FastAPI to serve the agentic engine asynchronously.
- **🎨 Premium UI:** A beautiful, responsive, glassmorphic React frontend stylized with Tailwind CSS.
- **📝 Structured Output:** Forces the LLM to output meticulously designed itineraries without markdown tables, prioritizing readability and aesthetic design.

---

## 🏗️ Architecture

1. **Frontend (`/frontend`)**: A React/Vite application providing a chat-like interface. It posts user queries to the backend and renders markdown responses dynamically.
2. **Backend (`/backend`)**: A FastAPI server that hosts the LangGraph AI workflow.
3. **Agent (`/backend/agent`)**: The core brain. It intercepts the user's prompt, injects system instructions, evaluates which tools are needed, executes the tools, and compiles the final result.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- API Keys for:
  - Groq (or OpenRouter)
  - OpenWeatherMap
  - ExchangeRate-API
  - Google Places API

### 1. Backend Setup
Navigate to the project root and create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

Navigate to the backend directory and install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file inside the `backend/` directory with your API keys:
```ini
GROQ_API_KEY=your_groq_api_key
OPENWEATHERMAP_API_KEY=your_weather_api_key
EXCHANGE_RATE_API_KEY=your_exchange_api_key
GPLACES_API_KEY=your_google_places_api_key
```

Start the FastAPI server:
```bash
uvicorn main:app --reload --port 8000
```
*The backend will now be running at `http://localhost:8000`.*

### 2. Frontend Setup
Open a **new** terminal window and navigate to the frontend directory:
```bash
cd frontend
```

Install the Node modules:
```bash
npm install
```

Start the Vite development server:
```bash
npm run dev
```
*The frontend will now be running at `http://localhost:5173`.*

---

## 💻 Usage
1. Open your browser and navigate to `http://localhost:5173`.
2. Type a complex travel prompt into the chat interface (e.g., *"Plan a 3-day luxury trip to Tokyo for 2 adults in November, including live weather expectations and costs in JPY."*)
3. The backend agent will autonomously trigger its weather and currency tools, aggregate the real-time data, and stream back a perfectly formatted, premium itinerary.

---

## 🛠️ Tech Stack
- **AI/Agent Framework:** LangChain, LangGraph
- **Backend:** FastAPI, Python, Pydantic
- **Frontend:** React, Vite, Tailwind CSS, Lucide Icons, React-Markdown
- **LLM Provider:** Groq (Llama-3 / Mixtral)

---

## 👤 Author
*Bhargav Nama* - Built as a showcase of Agentic AI Engineering and Full-Stack Development.
