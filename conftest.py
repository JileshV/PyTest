import pytest

@pytest.fixture(autouse=True,scope="class")       #yield_fixture() can also work
def setUp():                                       #scope=function runs both setup and teardown code for all tests
    print("Launch browser")                        #scope=session runs setup before test run and teardown after all tests are run
    print("Login")
    print("Browse product")
    yield
    print("Logoff")
    print("Close browser")