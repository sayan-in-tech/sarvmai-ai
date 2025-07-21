# 🚀 Deploy on Render.com
**Deployed Link** on: [Spelling Checker](https://sarvmai-ai.onrender.com)

# Indic Spellchecker Web App

A modern, multi-language spellchecker web service for Indic languages (Malayalam & Hindi), built with FastAPI. Sleek dark-mode web UI included!

---

## 🚀 Features
- **Spellcheck** for Malayalam and Hindi
- **Spelling Suggestions** for misspelled words
- **Modern Web UI** (dark mode, responsive)
- **REST API** for programmatic access
- **Easy Deployment** (local or Render.com)
- **No external dependencies** on other projects

---

## 🗂️ Project Structure
```
.
├── spellchecker_app.py         # FastAPI app
├── spellchecker_ml.py          # Spellchecker logic (Malayalam & Hindi)
├── pycache_cleaner.py          # Utility to auto-delete __pycache__
├── requirements.txt            # All dependencies
├── templates/
│   └── index.html              # Web UI
├── static/
│   └── style.css               # Web UI styles
├── data/
│   ├── ml_rootwords.txt        # Malayalam root words
│   └── hi_rootwords.txt        # Hindi root words
└── README.md
```

---

## 🛠️ Local Setup

1. **Clone the repo & enter the directory:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   uvicorn spellchecker_app:app --reload
   ```
4. **Open your browser:**
   - Go to [http://localhost:8000/](http://localhost:8000/)
   - Use the web UI to check and correct Malayalam or Hindi words!

---

## 🌐 API Usage

### Check Spelling
```http
POST /check
{
  "word": "मलयालम",
  "language": "hi"
}
```

### Get Suggestions
```http
POST /suggest
{
  "word": "മലായളം",
  "language": "ml"
}
```

### Check & Suggest (Combined)
```http
POST /check_and_suggest
{
  "word": "मलयालम",
  "language": "hi"
}
```

---