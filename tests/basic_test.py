from pythontestapplication import applicationfile2

import context 

def test_oursamplefunction():
    assert applicationfile2.convert("Johnny") == "Johnny"
