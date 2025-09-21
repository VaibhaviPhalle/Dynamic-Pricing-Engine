# Dynamic Pricing Engine - Scaffold

This repository is a scaffold for a Dynamic Pricing Engine (MVP).
It includes a simple FastAPI backend, a rule-based pricing engine, a placeholder ML model, sample data,
and CI + Docker examples.

## Structure
- backend/
  - app/
    - main.py            # FastAPI app
    - pricing_engine.py  # Core pricing logic (rule-based + ML wrapper)
    - model/
      - trainer.py      # Simple trainer for demo (scikit-learn)
  - requirements.txt    # Python dependencies
- data/
  - sample_data.csv     # Small sample dataset for testing
- frontend/
  - README.md           # Notes to scaffold a React frontend
- .github/workflows/ci.yml
- Dockerfile

## Quickstart (backend)
1. Create a venv: `python -m venv .venv && source .venv/bin/activate`
2. Install: `pip install -r backend/requirements.txt`
3. Run: `uvicorn backend.app.main:app --reload --port 8000`
4. Try: `POST http://localhost:8000/price` with JSON body like:
   {
     "base_price": 10.0,
     "demand": 120,
     "supply": 80,
     "time_of_day": 18,
     "competitor_price": 9.5
   }

## Notes
- The ML component is a simple placeholder using scikit-learn. For production, use a
  proper training pipeline, model versioning, monitoring, and more advanced algorithms (e.g., RL).
- This scaffold is intended to be a starting point for development and testing.
