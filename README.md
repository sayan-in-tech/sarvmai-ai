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

## 🚀 Deploy on Render.com

1. **Push your code to GitHub.**
2. **Create a new Web Service** on [Render](https://render.com/):
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn spellchecker_app:app --host 0.0.0.0 --port $PORT`
3. **Make sure your `data/`, `templates/`, and `static/` folders are committed!**
4. **Visit your Render URL** to use the app online.

---

## 📝 Adding More Languages
- Add a new rootwords file (e.g., `ta_rootwords.txt` for Tamil) in `data/`.
- Add a new class in `spellchecker_ml.py` (copy the pattern for Hindi/Malayalam).
- Register it in `spellchecker_app.py` under `SUPPORTED_LANGUAGES`.
- Enable it in the UI dropdown in `templates/index.html`.

---

## 🐞 Troubleshooting
- **FileNotFoundError:** Make sure your `data/` folder and rootwords files exist and are committed.
- **ModuleNotFoundError:** Check your imports and run `uvicorn` from the correct directory.
- **Render.com 404/502:** Check logs, ensure all files are present, and your start command is correct.
- **Web UI not updating:** Hard refresh your browser (Ctrl+Shift+R).

---

## 🙏 Credits
- [FastAPI](https://fastapi.tiangolo.com/)
- [marisa-trie](https://github.com/pytries/marisa-trie)
- [difflib](https://docs.python.org/3/library/difflib.html)
- [SCOWL Hindi Wordlist](https://github.com/kaustubhhiware/scowl-hindi-wordlist) (for Hindi rootwords)
- [LibIndic](https://github.com/libindic/libindic) (for inspiration)

---

## 💡 License
MIT or your preferred license. 