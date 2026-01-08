import pytest

def testLogin(setUp):
    print("Login successful")

def testLogout():
    print("Logout successful")

@pytest.mark.myTests
def testCalculate():
    assert 2+2 == 4