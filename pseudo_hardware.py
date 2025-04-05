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
            return "AUTHENTICATION SUCCESS"
        else:
            return "AUTHENTICATION FAIL"
        


#Mock serial class for creating hardware interface
class PseudoSerial:
    def __init__(self, port, baudrate, timeout):
        
        self.buffer = io.StringIO()
        self.last_command = ""

        self.auth = AuthenticationManager() #incorporate authentication manager test system

        #simulate bad connection (50% chance of bad connection)
        connectionChance = random.randint(0,1)
        if connectionChance == 1:
            self.status = True
        else:
            self.status = False


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


        self.buffer = io.StringIO(response + "\n")

    def readline(self):
        return self.buffer.readline().encode()
    
    def readlines(self):
        return [line.encode() for line in self.buffer.getvalue().splitlines()]
    
    def close(self):
        pass