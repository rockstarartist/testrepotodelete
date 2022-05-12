from pythontestapplication import applicationfile2

from .context import pythontestapplication


def test_oursamplefunction():
    assert applicationfile2.convert("Johhny") == "Johnny"
