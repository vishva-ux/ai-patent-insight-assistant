# 🔬 AI Patent Insight Assistant

> An NLP + LLM-powered tool to analyze technical patent documents and generate summarized insights using semantic search and intelligent document querying.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Hugging Face](https://img.shields.io/badge/HuggingFace-Transformers-orange?style=flat-square&logo=huggingface)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit)
![NLP](https://img.shields.io/badge/NLP-Semantic%20Search-green?style=flat-square)

---

## 📌 Features

- **Patent Analysis** — Paste or upload patent text and get AI-generated executive summaries, innovation breakdowns, and extracted claims
- **Semantic Search** — Search a patent corpus using natural language queries powered by sentence transformers (all-MiniLM-L6-v2)
- **Patent Comparison** — Compare two patents and compute their semantic similarity score with overlap analysis
- **Novelty Scoring** — Automatically score patents on technical novelty, prior art overlap, claim breadth, and commercial viability
- **Citation Impact Visualization** — View citation trends over time per patent

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| NLP Models | Hugging Face Transformers |
| Embeddings | `sentence-transformers` (all-MiniLM-L6-v2) |
| UI (Prototype) | HTML + CSS + Vanilla JS |
| Backend (Full) | Streamlit |
| Search Index | FAISS / ChromaDB |
| Summarization | BART / T5 (via Hugging Face) |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-patent-insight-assistant.git
cd ai-patent-insight-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the prototype (HTML)
Just open `index.html` in your browser — no setup needed.

### 4. Run the Streamlit app (full version)
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
ai-patent-insight-assistant/
├── index.html          # Frontend prototype (fully functional demo)
├── app.py              # Streamlit app entry point
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── src/
│   ├── analyzer.py     # Patent NLP analysis pipeline
│   ├── search.py       # Semantic search engine
│   └── embeddings.py   # Sentence transformer utilities
└── sample_patents/
    ├── patent_nlp.txt
    ├── patent_av.txt
    └── patent_blockchain.txt
```

---

## 💡 How It Works

1. **Input** — User pastes patent text or uploads a `.txt` / `.pdf` file
2. **NLP Parsing** — Extracts abstract, claims, and technical terminology using Hugging Face pipelines
3. **Summarization** — BART/T5 model generates a concise executive summary
4. **Embedding** — Sentence transformer encodes text into a dense vector
5. **Semantic Search** — FAISS index retrieves semantically similar patents
6. **Scoring** — Rule-based + ML scoring for novelty, overlap, and claim breadth

---

## 📷 Demo

Open `index.html` in any browser for a full interactive demo with:
- 3 sample patents preloaded
- Analyze, Search, and Compare tabs
- Animated insight cards and score bars

---

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License — free to use and modify.
# ai-patent-insight-assistant
