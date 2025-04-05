#Simulate real-time simulator for hardware-in-the-loop testing
#Allows for mock serial connection to be established
#Simulates necessary test systems for test suite (i.e. firmware manager, authentication manager, log manager, beam steering system)

import time
import io
import random
        

class AuthenticationManager:
    def __init__(self):
        self.authenticated = False

    def login(self, username, password):
        if username == "admin" and password == "pass123":
            self.authenticated = True
            print("AUTHENTICATION SUCCESS")
            return "AUTHENTICATION SUCCESS"
        else:
            return "AUTHENTICATION FAIL"
        

class FirmwareManager:
    def __init__(self):
        self.current_version = "v1.0"
        self.last_good_version = "v1.0"
        self.valid_firmware_uploaded = False
        self.failed_validation = False

    def upload(self, firmware_name):
        if "corrupted" in firmware_name:
            self.failed_validation = True
            print("UPLOAD FAILED: CORRUPTED FILE")
            return "UPLOAD FAILED: CORRUPTED FILE"
        self.valid_firmware_uploaded = True
        print("UPLOAD ACCEPTED")
        return "UPLOAD ACCEPTED"
    
    def apply(self):
        if self.failed_validation:
            self.current_version = self.last_good_version
            print("ROLLBACK TO v1.0")
            return "ROLLBACK TO v1.0"
        self.current_version = "v2.0"
        print("FIRMWARE UPDATED SUCCESSFULLY")
        return "FIRMWARE UPDATED SUCCESSFULLY"
    
    def get_version(self):
        return self.current_version


class LogManager:
    def __init__(self):
        self.logs = ["[0s] BOOT"]
        self.events = []
    
    def retrieve(self):
        print("\n".join(self.logs))
        print("LOGS RECEIVED")
        return "\n".join(self.logs)
    
    def get_status(self):
        print("STATUS: ALL SYSTEMS NORMAL")
        return "STATUS: ALL SYSTEMS NORMAL"
    

class BeamSteeringSystem:
    def __init__(self):
        self.theta = 0.0

    def set_beam(self, theta):
        self.theta = float(theta)
        print(f"BEAM SET TO {theta} degrees")
        return f"BEAM SET TO {theta}"
    
    def get_beam(self):
        #print(f"BEAM AT: {self.theta} degrees")
        return f"BEAM AT: {self.theta}"
    

#Mock serial class for creating hardware interface
class PseudoSerial:
    def __init__(self, port, baudrate, timeout):
        
        self.buffer = io.StringIO()
        self.last_command = ""

        self.auth = AuthenticationManager() #incorporate authentication manager test system
        self.firmware = FirmwareManager() #incorporate firmware manager test system
        self.logs = LogManager() #incorporate logging manager test system
        self.beam = BeamSteeringSystem() #incorporate beam steering test system


        #simulate bad connection (50% chance of bad connection)
        connectionChance = random.randint(0,1)
        if connectionChance == 1:
            self.status = True
        else:
            self.status = True #set to False to give 50% chance of bad connection


    def checkConnection(self):
        if self.status == True:
            return True
        else:
            return False, "FAILED SERIAL CONNECTION"


    def write(self, command_bytes):
        
        command = command_bytes.decode().strip()
        self.last_command = command

        parts = command.split()
        response = ""


    #For Authentication Manager
        if command.startswith("OTA_AUTH"):
            response = self.auth.login(parts[1], parts[2])
    
    #For Firmware Manager
        elif command.startswith("OTA_UPLOAD"):
            response = self.firmware.upload(parts[-1])
        elif command.startswith("OTA_APPLY"):
            response = self.firmware.apply()
        elif command.startswith("FIRMWARE_VERSION"):
            response = self.firmware.get_version()

    #For Logging Manager
        elif command.startswith("GET_LOG"):
            response = self.logs.retrieve()
        elif command.startswith("STATUS_CHECK"):
            response = self.logs.get_status()

    #For Beam Steering System
        elif command.startswith("SET_BEAM"):
            response = self.beam.set_beam(parts[1])
        elif command.startswith("GET_BEAM"):
            response = self.beam.get_beam()


        self.buffer = io.StringIO(response + "\n")

    def readline(self):
        return self.buffer.readline().encode()
    
    def readlines(self):
        return [line.encode() for line in self.buffer.getvalue().splitlines()]
    
    def close(self):
        pass