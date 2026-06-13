# weather-agent-3layer-system



# 🌦️ Weather Agent (3-Layer System)

A minimal but structured **3-layer weather agent system** that takes natural language input from the user, processes it through a backend agent, calls an external weather API, and returns real-time weather information.

---

# 🚀 Overview

This project demonstrates a simple **agent-based architecture** without using LLMs.  
The backend acts as a lightweight decision-making agent that:
- interprets user input
- decides when to call a tool (Weather API)
- returns a formatted response to the frontend

---

# 🧠 System Architecture

```text
User   (enters a query)
  ↓
Frontend (HTML + JavaScript) (capture and send request to backend)
  ↓
Backend (FastAPI - Agent Layer) (agent process, extract city, decide to call WeatherAPI, sends request to backend)
  ↓
Weather API (Tool Layer)  (returns JSON)
  ↓
Backend (formats response)
  ↓
Frontend (displays to user)
  ↓
User












weather-agent/
│
├── frontend/
│   ├── index.html       # UI structure
│   ├── app.js           # API calls + UI logic
│   └── style.css        # Simple styling
│
├── backend/
│   ├── main.py          # FastAPI entry point
│   ├── agent.py         # Agent logic (decision-making)
│   └── weather_api.py   # External API integration
│
├── requirements.txt
└── README.md