# Pixel

FastAPI backend that generates Product Requirement Documents from product ideas using LLMs.


## Project Structure
```
pixel-backend/
├── app/
│   ├── api/
│   │   └── generate.py          # API endpoint handlers
│   ├── core/
│   │   ├── model.py              # Pydantic models
│   │   └── prompt.py             # LLM prompt logic
│   └── __init__.py
├── main.py                       # FastAPI app entry point
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
├── .env.example                  # Environment variables template
└── README.md
```

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Run server
uvicorn main:app
```

API will be available at `http://localhost:8000`

## API Usage

**Generate PRD:** `POST /api/generate`
```json
{
  "idea": "Your product idea here"
}
```

**Health Check:** `GET /health`