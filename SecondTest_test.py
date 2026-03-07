def testLogin():
    print("Login successful")

def testLogout():
    print("Logout successful")

def testCalculate():
    assert 2+2 == 4

def testErrorMsg():
    a = 4
    b = 10
    assert a == b, "a is not equal to b"