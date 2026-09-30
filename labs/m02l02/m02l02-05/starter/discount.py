def discounted(price, percent):
    """Price in pence after a whole number percentage discount."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between zero and a hundred")
    return round(price * (100 - percent) / 100)
