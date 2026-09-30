from invite import code


class RedChoice:
    def choice(self, options):
        return "red"


def test_code_uses_the_generator_result():
    assert code(RedChoice()) == "red"
