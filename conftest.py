#Configure pytest fixture for test suite

import pytest
from pseudo_hardware import PseudoConnection

@pytest.fixture(scope="session")
def connection_interface():

    #setup connection to device
    print("\n[SETUP] Creating a wireless connection to antenna system...")
    connection_interface = PseudoConnection('Wireless?', 9600, timeout=2)

    yield connection_interface

    print("\n[TEARDOWN] Closing wireless connection...")
    connection_interface.close()
