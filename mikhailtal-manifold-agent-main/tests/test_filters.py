from bot.filters import filter_mikhailtal_markets

def test_filter_mikhailtal_markets():
    markets = [
        {"creatorUsername": "MikhailTal", "isResolved": False},
        {"creatorUsername": "OtherUser", "isResolved": False},
        {"creatorUsername": "MikhailTal", "isResolved": True}
    ]

    filtered = filter_mikhailtal_markets(markets)
    assert len(filtered) == 1
    assert filtered[0]["creatorUsername"] == "MikhailTal"
