# run_example.py - quick demo without starting the server
from backend.app.pricing_engine import PricingEngine
def main():
    engine = PricingEngine()
    req = dict(base_price=10.0, demand=120, supply=80, time_of_day=18, competitor_price=9.5)
    price, strat, reason = engine.suggest_price(req)
    print(f"Suggested price: {price} | strategy={strat} | reason={reason}")
if __name__ == '__main__':
    main()
