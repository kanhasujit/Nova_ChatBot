# ✦ Nova — AI Chatbot

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/🦜_LangChain-1C3C3C?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)
![LLaMA](https://img.shields.io/badge/LLaMA_3.1-0467DF?style=for-the-badge&logo=meta&logoColor=white)

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Nova_ChatBot-7c5cfc?style=for-the-badge)](https://huggingface.co/spaces/Scizzor/bot_deploy)

> 🎉 **My first project built with [LangChain](https://python.langchain.com)** — the leading framework for building LLM-powered applications.

A sleek, dark-themed conversational AI chatbot with **typewriter-style streaming**, full **conversation memory**, and a polished custom UI — all powered by **LangChain + Groq**.

---

## 🦜 Why LangChain?

This project was my first hands-on experience with **LangChain** — and it made building an AI chatbot remarkably simple.

| What LangChain handled | Without LangChain |
|---|---|
| Connecting to Groq's LLaMA model | Manual HTTP requests to Groq API |
| Passing conversation history for memory | Manually formatting message arrays |
| Swapping models in one line | Rewriting integration code |
| `HumanMessage` / `AIMessage` types | Custom dict structures |

LangChain abstracts all the complexity — you focus on building, not plumbing.

---

## ✨ Features

- 🦜 **LangChain-powered** — clean, provider-agnostic LLM integration
- 🧠 **Conversation memory** — full chat history passed on every turn
- ⌨️ **Typewriter effect** — response appears character by character with a blinking `▌` cursor
- 🎨 **Custom dark UI** — gradient header, animated status dot, no default Streamlit look
- ⚡ **Groq LLaMA 3.1** — ultra-fast inference

---

## 🛠️ Tech Stack

| | Tool |
|---|---|
| 🦜 **LLM Framework** | **LangChain** (`langchain-groq`, `langchain-core`) |
| ⚡ LLM Provider | Groq — LLaMA 3.1 8B Instant |
| 🖥️ UI | Streamlit |
| 🔐 Env vars | python-dotenv |

---

## 📦 Installation

```bash
# 1. Clone
git clone https://github.com/your-username/nova-chatbot.git
cd nova-chatbot

# 2. Create virtual environment
python -m venv myenv
myenv\Scripts\activate        # Windows
source myenv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install streamlit langchain langchain-groq langchain-core python-dotenv
```

---

## 🔑 Setup API Key

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free key at → https://console.groq.com

---

## ▶️ Run

```bash
streamlit run chatbot_app.py
```
Open → `http://localhost:8501`

---

## 🦜 LangChain in This Project

Here's exactly how LangChain is used — great reference for your next project:

```python
from langchain_groq import ChatGroq                          # LangChain's Groq integration
from langchain_core.messages import HumanMessage, AIMessage  # LangChain message types

# 1. Initialize the model — swap "groq" for "openai", "anthropic" etc. anytime
llm = ChatGroq(model="llama-3.1-8b-instant", api_key="...")

# 2. Build message history (this gives the model memory)
messages = [
    HumanMessage(content="Hello!"),
    AIMessage(content="Hi! How can I help?"),
    HumanMessage(content="What is BERT?")
]

# 3. Invoke — LangChain handles the API call, formatting, and response parsing
response = llm.invoke(messages)
print(response.content)
```

**Memory** works by passing the full `messages` list every time — LangChain's message types make this clean and readable.

---

## 📁 Project Structure

```
nova-chatbot/
├── chatbot_app.py   # Main app
├── .env             # API key (never commit!)
├── .gitignore
└── README.md
```

---

## 🔒 .gitignore

```
.env
myenv/
__pycache__/
*.pyc
```

---

## 🧩 Key LangChain Concepts Learned

- **Chat Models** — `ChatGroq` wraps the Groq API in LangChain's standard interface
- **Message Types** — `HumanMessage` and `AIMessage` structure the conversation history
- **Provider Swapping** — replacing Groq with OpenAI or Anthropic takes one import change
- **Memory Pattern** — passing full message history = conversational memory, no extra setup needed

---

## 🚀 What's Next with LangChain

Now that you know the basics, here's where to go next:

| Feature | LangChain Tool |
|---|---|
| Web search / tools | `langchain.agents` + `create_agent` |
| Auto-summarize long chats | `SummarizationMiddleware` |
| RAG (chat with your docs) | `langchain.vectorstores` |
| Structured output | `llm.with_structured_output()` |

---

## 📄 License

MIT — free to use and build on.
