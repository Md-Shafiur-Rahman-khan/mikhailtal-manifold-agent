import requests
from bot.config import MANIFOLD_API_KEY

BASE_URL = "https://api.manifold.markets/v0"

class ManifoldClient:
    def __init__(self):
        self.headers = {
            "Authorization": f"Key {MANIFOLD_API_KEY}"
        }

    def get_markets(self, limit=100):
        response = requests.get(
            f"{BASE_URL}/markets",
            headers=self.headers,
            params={"limit": limit}
        )
        response.raise_for_status()
        return response.json()

    def place_bet(self, market_id, outcome, amount):
        payload = {
            "contractId": market_id,
            "outcome": outcome,
            "amount": int(amount)
        }
        response = requests.post(
            f"{BASE_URL}/bet",
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()

