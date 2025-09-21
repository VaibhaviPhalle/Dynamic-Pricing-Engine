import math
import numpy as np

class PricingEngine:
    """Simple pricing engine with rule-based and ML-based fallback.

    Methods:
    - suggest_price(inputs): returns (price, strategy_name, reason)
    """
    def __init__(self, ml_model=None):
        # ml_model can be a callable that predicts a multiplier or price
        self.ml_model = ml_model

    def suggest_price(self, inputs: dict):
        # Try rule-based first
        rb = self.rule_based(inputs)
        # If conditions allow, use ML to refine (placeholder)
        if self.ml_model:
            ml_price = self._ml_predict_price(inputs)
            # choose the prediction with higher expected revenue (simple heuristic)
            if ml_price > rb * 0.95 and ml_price < rb * 1.2:
                return ml_price, "ml_based", "ML adjusted price within safe bounds"
        return rb, "rule_based", "Rule-based price chosen"

    def rule_based(self, inputs: dict):
        base = float(inputs.get("base_price", 1.0))
        demand = float(inputs.get("demand", 1.0))
        supply = float(inputs.get("supply", 1.0))
        time_of_day = int(inputs.get("time_of_day", 12))
        competitor = inputs.get("competitor_price", None)

        # simple surge factor
        ratio = (demand + 1e-6) / (supply + 1e-6)
        surge = 1.0
        if ratio > 1.2:
            surge += min(0.5, (ratio - 1.2) * 0.5)  # cap surge
        elif ratio < 0.8:
            surge -= min(0.4, (0.8 - ratio) * 0.5)

        # time-based multiplier (peak hours 17-20)
        if 17 <= time_of_day <= 20:
            time_mult = 1.1
        else:
            time_mult = 1.0

        price = base * surge * time_mult

        # competitor adjustment (stay slightly below if competitor exists)
        if competitor is not None:
            # avoid undercutting too much
            price = min(price, competitor * 0.98 + 0.01)

        # floor and ceiling
        price = max(price, base * 0.5)
        price = min(price, base * 3.0)
        return round(price, 4)

    def _ml_predict_price(self, inputs: dict):
        # ml_model is expected to accept a 1D feature array and return a price
        feat = self._featurize(inputs)
        pred = self.ml_model(np.array(feat).reshape(1, -1))[0]
        return float(pred)

    def _featurize(self, inputs: dict):
        base = float(inputs.get("base_price", 1.0))
        demand = float(inputs.get("demand", 1.0))
        supply = float(inputs.get("supply", 1.0))
        time_of_day = int(inputs.get("time_of_day", 12))
        competitor = inputs.get("competitor_price", base)
        ratio = (demand + 1e-6) / (supply + 1e-6)
        return [base, demand, supply, time_of_day, competitor, ratio]
