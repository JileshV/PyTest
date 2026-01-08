import pytest

def testLogin():
    print("Login successful")

@pytest.mark.myTests
def testLogout():
    print("Logout successful")

@pytest.mark.skip
def testCalculate():
    assert 2+2 == 4