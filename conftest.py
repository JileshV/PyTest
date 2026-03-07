import pytest

@pytest.fixture()       #yield_fixture() can also work
def setUp():
    print("Launch browser")
    print("Login")
    print("Browse product")
    yield
    print("Logoff")
    print("Close browser")