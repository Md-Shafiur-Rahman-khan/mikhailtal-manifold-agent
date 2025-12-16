from bot.config import MAX_BET, KELLY_FRACTION

def fractional_kelly(true_p: float, market_p: float) -> float:
    """
    Fractional Kelly bet sizing.
    """
    edge = true_p - market_p
    if edge <= 0:
        return 0

    raw_kelly = edge / (1 - market_p)
    bet = raw_kelly * KELLY_FRACTION * MAX_BET

    return max(1, min(MAX_BET, bet))
