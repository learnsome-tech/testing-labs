def pay(gateway, pence, reference):
    return gateway.charge(pence, reference)["reference"]
