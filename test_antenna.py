#Test suite of hypothetical antenna system to verify satisfaction of functional requirements
import time
import pytest

def test_serial_connection(connection_interface):

    #Verify that serial connection is made
    connected = connection_interface.checkConnection()
    assert connected == True, f"No serial connection found, stopping test suite"
    print("\nSerial connection found, proceeding to next test cases...")


# def test_ota_authentication(connection_interface):
    
#     #Verify that serial connection was prior made
#     connected = connection_interface.checkConnection()
#     assert connected == True, f"No serial connection found, test cannot proceed"

#     print("\n[TEST] OTA authentication...")
#     connection_interface.write(b'OTA_AUTH admin pass123\n')
#     time.sleep(0.5)
#     response = connection_interface.readline().decode().strip()
#     assert "AUTHENTICATION SUCCESS" in response, \
#         f"Expected OTA authentication to succeed, got '{response}'"
    

# # def test_ota_authentication_FAIL(connection_interface):

# #     #Verify that serial connection was prior made
# #     connected = connection_interface.checkConnection()
# #     assert connected == True, f"No serial connection found, test cannot proceed"
    
# #     print("\n[TEST] OTA authentication...")
# #     connection_interface.write(b'OTA_AUTH admin WRONGPASS\n')
# #     time.sleep(0.5)
# #     response = connection_interface.readline().decode().strip()
# #     assert "AUTHENTICATION SUCCESS" in response, \
# #         f"Expected OTA authentication to succeed, got '{response}'"
    

# def test_ota_rollback_on_fail(connection_interface):

#     #Verify that serial connection was prior made
#     connected = connection_interface.checkConnection()
#     assert connected == True, f"No serial connection found, test cannot proceed"

#     print("\n[TEST] OTA rollback on failure...")
#     connection_interface.write(b'OTA_UPLOAD corrupted_firmware.bin\n')
#     time.sleep(0.5)
#     connection_interface.write(b'OTA_APPLY\n')
#     time.sleep(0.5)
#     connection_interface.write(b'FIRMWARE_VERSION\n')
#     version = connection_interface.readline().decode().strip()
#     assert "v1.0" in version, f"Expected fallback to stable firmware v1.0, got '{version}'"


# def test_log_retrieval(connection_interface):

#     #Verify that serial connection was prior made
#     connected = connection_interface.checkConnection()
#     assert connected == True, f"No serial connection found, test cannot proceed"

#     print("\n[TEST] Log retrieval over serial connection...")
#     connection_interface.write(b'GET_LOG\n')
#     logs = connection_interface.readlines()
#     logs_decoded = [log.decode() for log in logs]
#     assert any("BOOT" in line for line in logs_decoded), "Expected log to include 'BOOT' event"


# def test_status_check_packet(connection_interface):

#     #Verify that serial connection was prior made
#     connected = connection_interface.checkConnection()
#     assert connected == True, f"No serial connection found, test cannot proceed"

#     print("\n[TEST] Running status check...")
#     connection_interface.write(b'STATUS_CHECK\n')
#     response = connection_interface.readline().decode().strip()
#     assert "STATUS:" in response or "ALL SYSTEMS NORMAL" in response, \
#     f"Expected valid status message, got '{response}'"


def test_beam_position_query_time(connection_interface):

    #Verify that serial connection was prior made
    connected = connection_interface.checkConnection()
    assert connected == True, f"No serial connection found, test cannot proceed"

    print("\n[TEST] Beam query response time...")
    connection_interface.write(b'GET_BEAM\n')
    t0 = time.time()
    time.sleep(2) #induces failure if > 3 seconds
    response = connection_interface.readline().decode().strip()
    t1 = time.time()
    print(f"Time to respond: {t1 - t0} seconds")
    assert t1 - t0 <= 3, f"Beam query took too long: {t1 - t0: .2f}s"


def test_beam_position_query_time_LAG(connection_interface):

    #Verify that serial connection was prior made
    connected = connection_interface.checkConnection()
    assert connected == True, f"No serial connection found, test cannot proceed"

    print("\n[TEST] Beam query response time...")
    connection_interface.write(b'GET_BEAM\n')
    t0 = time.time()
    time.sleep(4) #induces failure if > 3 seconds
    response = connection_interface.readline().decode().strip()
    t1 = time.time()
    print(f"Time to respond: {t1 - t0} seconds")
    assert t1 - t0 <= 3, f"Beam query took too long: {t1 - t0: .2f}s"


# def test_manual_beam_command(connection_interface):

#     #Verify that serial connection was prior made
#     connected = connection_interface.checkConnection()
#     assert connected == True, f"No serial connection found, test cannot proceed"

#     print("\n[TEST] Manual beam pointing...")
#     connection_interface.write(b'GET_BEAM\n')
#     initial_position = connection_interface.readline().decode().strip()
#     print(f"BEAM AT: {initial_position}")

#     connection_interface.write(b'SET_BEAM 45\n')
#     intended_position = connection_interface.readline().decode().strip()
#     time.sleep(1)

#     connection_interface.write(b'GET_BEAM\n')
#     response = connection_interface.readline().decode().strip()

#     current_position = float(response.split()[2])
#     current_position = current_position + 0.5 #some pertubuation or error; induces failure if > 1 degree
#     print(f"BEAM AT: {current_position}")

#     assert abs((current_position) - abs(float(intended_position.split()[3]))) <= 1, f"Theta deviation too large: got {current_position}"
