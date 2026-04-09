import pytest

def testLogin(setUp):       #If used 'autouse=True' is used in 'SetUp' fixture
    print("Login successful")

def testLogout():
    print("Logout successful")

@pytest.mark.myTests
def testCalculate():
    assert 2+2 == 4