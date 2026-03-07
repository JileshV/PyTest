import pytest

@pytest.mark.parametrize("a,b,c",[(4,2,7),(22,21,43),(111,156,267)])
def testCalculate(a,b,c):
    assert a+b == c