def refund(paid, returned, restocking_fee=0):
    """Pence to hand back for a returned order."""
    if returned > paid:
        raise ValueError("cannot refund more than was paid")
    if restocking_fee:
        return paid - returned - restocking_fee
    return paid - returned
