#Test suite of hypothetical antenna system to verify satisfaction of functional requirements
import time

def test_serial_connection(connection_interface):

    #Verify that serial connection is made
    connected = connection_interface.checkConnection()
    assert connected == True, f"No serial connection found, stopping test suite"
    print("\nSerial connection found, proceeding to next test cases...")


def test_ota_authentication(connection_interface):
    
    #Verify that serial connection was prior made
    connected = connection_interface.checkConnection()
    assert connected == True, f"No serial connection found, test cannot proceed"

    print("\n[TEST] OTA authentication...")
    connection_interface.write(b'OTA_AUTH admin pass123\n')
    time.sleep(0.5)
    response = connection_interface.readline().decode().strip()
    assert "AUTHENTICATION SUCCESS" in response, \
        f"Expected OTA authentication to succeed, got '{response}'"
    

def test_ota_authentication_FAIL(connection_interface):

    #Verify that serial connection was prior made
    connected = connection_interface.checkConnection()
    assert connected == True, f"No serial connection found, test cannot proceed"
    
    print("\n[TEST] OTA authentication...")
    connection_interface.write(b'OTA_AUTH admin WRONGPASS\n')
    time.sleep(0.5)
    response = connection_interface.readline().decode().strip()
    assert "AUTHENTICATION SUCCESS" in response, \
        f"Expected OTA authentication to succeed, got '{response}'"