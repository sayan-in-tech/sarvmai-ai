# Malayalam Spellchecker Web Service

This is a simple FastAPI web service for Malayalam spell checking and suggestions, powered by the LibIndic spellchecker.

## Features
- Check if a Malayalam word is spelled correctly
- Get spelling suggestions for a word
- Combined check and suggest endpoint

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Make sure the `other-project` folder is present at the same level as `main-project`.

## Running the App

```bash
uvicorn spellchecker_app:app --reload
```

## API Endpoints

### POST `/check`
**Request:**
```json
{
  "word": "മലയാളം"
}
```
**Response:**
```json
{
  "word": "മലയാളം",
  "correct": true
}
```

### POST `/suggest`
**Request:**
```json
{
  "word": "മലായളം"
}
```
**Response:**
```json
{
  "suggestions": ["മലയാളം", ...]
}
```

### POST `/check_and_suggest`
**Request:**
```json
{
  "word": "മലായളം"
}
```
**Response:**
```json
{
  "status": 0,
  "suggestions": ["മലയാളം", ...]
}
```

## Notes
- This service is for Malayalam language spell checking.
- The spellchecker logic is imported from the LibIndic project in `../other-project/libindic/spellchecker`. 