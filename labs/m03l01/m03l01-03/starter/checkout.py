from gateway import GatewayTimeout


def pay(gateway, pence, reference):
    """Charge a basket, or report that the gateway did not answer."""
    try:
        receipt = gateway.charge(pence, reference)
    except GatewayTimeout:
        return None
    return receipt["reference"]
