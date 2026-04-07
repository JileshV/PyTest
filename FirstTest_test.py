import pytest

def testLogin(setUp):
    print("Login successful")

@pytest.mark.xfail
def testLogout(setUp):
    print("Logout successful")
    assert False

@pytest.mark.xfail
def testCalculate():
    assert 2+2 == 4