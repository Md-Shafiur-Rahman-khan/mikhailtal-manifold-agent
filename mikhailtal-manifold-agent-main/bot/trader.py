import time
from bot.client import ManifoldClient
from bot.filters import filter_mikhailtal_markets
from bot.strategy import final_probability
from bot.sizing import fractional_kelly
from bot.config import MIN_EDGE

class Trader:
    def __init__(self, use_llm=False):
        self.client = ManifoldClient()
        self.use_llm = use_llm

    def run(self):
        markets = self.client.get_markets()
        targets = filter_mikhailtal_markets(markets)

        for market in targets:
            market_p = market["probability"]
            true_p = final_probability(
                market_p,
                use_llm=self.use_llm,
                question=market.get("question", ""),
                description=market.get("description", "")
            )

            edge = true_p - market_p
            if abs(edge) < MIN_EDGE:
                continue

            outcome = "YES" if edge > 0 else "NO"
            amount = fractional_kelly(true_p, market_p)

            if amount > 0:
                self.client.place_bet(
                    market_id=market["id"],
                    outcome=outcome,
                    amount=amount
                )

                time.sleep(1)  # API safety
