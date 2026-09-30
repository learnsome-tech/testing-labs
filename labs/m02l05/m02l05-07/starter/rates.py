RATES = {"EUR": 1.178, "USD": 1.271}


def rate_for(currency):
    """Pence per penny for one currency, or a KeyError naming it."""
    if currency not in RATES:
        raise KeyError(f"no rate for {currency}")
    return RATES[currency]


def convert(pence, currency):
    """Pence converted at today's rate, as a float."""
    return pence * rate_for(currency)
