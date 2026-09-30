class Gateway:
    """The real client: charge returns a receipt, or raises."""

    def charge(self, pence, reference):
        raise RuntimeError("this would reach the network")
