# EstateIQ — Real Estate Research Agent

> An AI-powered chatbot that lets you paste real estate article URLs, indexes them into a vector database, and answers your questions grounded in those sources.

---

## Demo

<img width="1362" height="638" alt="image" src="https://github.com/user-attachments/assets/1c854740-7809-40c8-ad59-af15169f2261" />


## Features

- Paste up to 3 real estate article URLs and process them in one click
- Content is scraped, chunked, embedded, and stored in a local Chroma vector database
- Ask natural language questions — answers are grounded in the loaded articles with source citations
- Clean, professional chat UI built from scratch (no Streamlit)
- Fully local vector store — no external database needed

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Groq API — Llama 3.3 70B Versatile |
| RAG Framework | LangChain |
| Vector Store | Chroma DB (local) |
| Embeddings | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| Web Scraping | LangChain UnstructuredURLLoader |
| Backend API | Flask + Flask-CORS |
| Frontend UI | Vanilla HTML, CSS, JavaScript |

---

## Project Structure
real-estate-research-agent/
├── app.py                  # Flask backend — serves UI and exposes /process and /answer endpoints
├── rag.py                  # Core RAG logic — scraping, chunking, embedding, retrieval, generation
├── prompt.py               # LangChain prompt templates
├── main.py                 # Original Streamlit UI (still works independently)
├── estateiq_ui.html        # Custom chat UI (served by Flask at localhost:5000)
├── requirements.txt        # Python dependencies
├── .env                    # API keys — never committed to git
├── .gitignore
└── resources/
└── vectorstore/        # Chroma DB files (auto-created on first run, not committed)
---

## How It Works
User pastes URLs
│
▼
UnstructuredURLLoader scrapes article content
│
▼
RecursiveCharacterTextSplitter chunks text (1000 chars)
│
▼
HuggingFace Embeddings converts chunks to vectors
│
▼
Chroma DB stores vectors locally
│
▼
User asks a question
│
▼
Chroma retrieves top-k relevant chunks
│
▼
LangChain RetrievalQAWithSourcesChain sends chunks + question to Groq
│
▼
Llama 3.3 70B generates a grounded answer with source citations
---

## Setup & Installation

### Prerequisites
- Python 3.10 or higher
- A free Groq API key from [console.groq.com](https://console.groq.com)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/real-estate-research-agent.git
cd real-estate-research-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your environment variables

Create a `.env` file in the project root:
GROQ_API_KEY=your_groq_api_key_here
### 4. Run the app

```bash
python app.py
```

### 5. Open in browser
---

## Usage

1. Paste one, two, or three real estate article URLs into the sidebar
2. Click **Process URLs** — the app scrapes, chunks, embeds, and indexes the content
3. Type any question in the chat box and press Enter
4. The answer appears with source citations showing which article it came from

### Example questions to try
- *What are the current property price trends?*
- *Which locations are seeing the most demand?*
- *What does the article say about home loan interest rates?*
- *Summarise all the loaded sources*

---

## Running the Original Streamlit UI

The original Streamlit version still works independently:

```bash
streamlit run main.py
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |

---

## Future Improvements

- [ ] Support for PDF uploads alongside URLs
- [ ] Persistent chat history across sessions
- [ ] Multiple collections / saved research sessions
- [ ] Deploy to cloud (Render / Railway / AWS)
- [ ] Add authentication for multi-user access

---

## Author

Built by Yash R Palde — [LinkedIn](www.linkedin.com/in/yash-palde-612b99333) · [GitHub](https://github.com/YashPalde2412)

---

## License

MIT License — free to use and modify.
