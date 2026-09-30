def pay(gateway, pence, reference):
    receipt = gateway.charge(pence, reference)
    return receipt["id"]
