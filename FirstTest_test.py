import pytest

def testLogin():
    print("Login successful")

@pytest.mark.xfail
def testLogout():
    print("Logout successful")
    assert False

@pytest.mark.xfail
def testCalculate():
    assert 2+2 == 4