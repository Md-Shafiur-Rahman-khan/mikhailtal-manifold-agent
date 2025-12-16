from bot.config import TARGET_CREATOR

def filter_mikhailtal_markets(markets):
    """
    Filters markets to only:
    - Created by MikhailTal
    - Not resolved
    """
    return [
        m for m in markets
        if m.get("creatorUsername") == TARGET_CREATOR
        and not m.get("isResolved", False)
    ]
