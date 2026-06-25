# 🎙️ AI Voice Agent SaaS

A production-grade AI Voice Agent with hands-free Hinglish conversation support.

## ✨ Features
- 🔐 JWT Authentication (Register / Login)
- 💬 AI Chat powered by Groq LLM (Llama 3)
- 🎙️ Voice input via Speech Recognition
- 🔊 Female Hinglish voice output via Sarvam AI
- 🤝 Hands-free continuous conversation mode
- ⚡ Interrupt AI mid-speech and take over
- 💾 Persistent conversation history in PostgreSQL
- 👥 Multi-user support

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Backend | FastAPI, Python |
| Database | PostgreSQL, SQLAlchemy |
| Auth | JWT |
| AI | Groq LLM (Llama 3.3) |
| Voice | Sarvam AI (Hinglish TTS) |
| Frontend | React, Tailwind CSS |

## 🚀 Running Locally

### Backend
cd Backend
pip install -r requirements.txt
uvicorn app.main:app --reload

### Frontend
cd Frontend
npm install
npm run dev
