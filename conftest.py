#Configure pytest fixture for test suite

import pytest
from pseudo_hardware import PseudoSerial

@pytest.fixture(scope="session")
def connection_interface():

    #define serial connection to a command line interface
    print("\n[SETUP] Creating a serial connection to antenna system...")
    connection_interface = PseudoSerial('COM9', 9600, timeout=2)

    yield connection_interface

    print("\n[TEARDOWN] Closing serial connection...")
    connection_interface.close()
