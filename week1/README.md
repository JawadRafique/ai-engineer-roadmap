# Motivational Quotes FastAPI Server

## Goal
- Code a simple FastAPI Server to display a motivational Quote
- Build a simple search engine using Chroma or Qdrant

## Checklist
- [x] FastAPI server created
- [x] Motivational quotes displayed via API
- [x] Quotes loaded into ChromaDB collection
- [x] Search endpoint implemented using ChromaDB

## Setup

### 1. Create a virtual environment (recommended)

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 2. Install required libraries

You can install all dependencies at once:

```bash
pip install -r requirements.txt
```

### 3. Start the server

```bash
uvicorn week1.main:app --reload
```

### 4. Access endpoints
   - `GET /quotes?quote_context=your+search+terms` — Search for quotes

## Notes
- Python 3.12 recommended for ChromaDB compatibility
- Quotes are loaded from `quotes.txt` on startup
