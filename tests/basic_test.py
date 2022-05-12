import context

from pythontestapplication import applicationfile2


def test_oursamplefunction():
    assert applicationfile2.convert("Johnny") == "Johnny"
