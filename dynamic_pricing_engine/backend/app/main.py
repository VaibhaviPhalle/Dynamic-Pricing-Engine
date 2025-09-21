from fastapi import FastAPI
from pydantic import BaseModel
from .pricing_engine import PricingEngine

app = FastAPI(title="Dynamic Pricing Engine - API")
engine = PricingEngine()

class PriceRequest(BaseModel):
    base_price: float
    demand: int
    supply: int
    time_of_day: int = 12
    competitor_price: float = None
    customer_segment: str = "default"

class PriceResponse(BaseModel):
    suggested_price: float
    strategy: str
    reason: str

@app.post("/price", response_model=PriceResponse)
async def get_price(req: PriceRequest):
    suggested_price, strategy, reason = engine.suggest_price(req.dict())
    return PriceResponse(suggested_price=suggested_price, strategy=strategy, reason=reason)

@app.get("/health")
async def health():
    return {"status": "ok"}
