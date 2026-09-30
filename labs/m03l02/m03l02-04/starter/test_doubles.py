from checkout import pay

class StubGateway:
    def charge(self, pence, reference):
        return {"reference": reference}

class SpyGateway:
    def __init__(self): self.calls = []
    def charge(self, pence, reference):
        self.calls.append((pence, reference))
        return {"reference": reference}

def test_a_stub_lets_you_check_the_answer():
    assert pay(StubGateway(), 1000, "abc") == "abc"

def test_a_spy_lets_you_check_the_request():
    spy = SpyGateway()
    pay(spy, 1000, "abc")
    assert spy.calls == [(1000, "abc")]
