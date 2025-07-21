import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import pathlib

# Import the local spellchecker module (to be created)
from main_project.spellchecker_ml import MalayalamSpellChecker

app = FastAPI(title="Indic Spellchecker API")

SUPPORTED_LANGUAGES = {
    'ml': {
        'name': 'Malayalam',
        'spellchecker': MalayalamSpellChecker(),
    },
    # Add more languages here in the future
}

class SpellCheckRequest(BaseModel):
    word: str
    language: str = 'ml'

class SuggestionResponse(BaseModel):
    suggestions: List[str]

@app.post("/check")
def check_spelling(request: SpellCheckRequest):
    lang = request.language
    if lang not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Language '{lang}' not supported.")
    spellchecker = SUPPORTED_LANGUAGES[lang]['spellchecker']
    result = spellchecker.check(request.word)
    return {"word": request.word, "correct": result, "language": lang}

@app.post("/suggest", response_model=SuggestionResponse)
def suggest_spelling(request: SpellCheckRequest):
    lang = request.language
    if lang not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Language '{lang}' not supported.")
    spellchecker = SUPPORTED_LANGUAGES[lang]['spellchecker']
    suggestions = spellchecker.suggest(request.word)
    return {"suggestions": suggestions}

@app.post("/check_and_suggest")
def check_and_suggest(request: SpellCheckRequest):
    lang = request.language
    if lang not in SUPPORTED_LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Language '{lang}' not supported.")
    spellchecker = SUPPORTED_LANGUAGES[lang]['spellchecker']
    result = spellchecker.check_and_generate(request.word)
    result['language'] = lang
    return result

# Static and template serving
BASE_DIR = pathlib.Path(__file__).parent
static_dir = BASE_DIR / "static"
templates_dir = BASE_DIR / "templates"

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 