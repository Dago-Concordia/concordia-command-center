import serial
import time
from threading import *

class Arduino:
    def __init__(self):
        self.command = "!def#"
    
    def sendCommand(self, cmd):
        # cmd = "!help#"
        self.command = cmd
        Thread(target=self.write_read).start()

    def write_read(self):
        if hasattr(self, 'arduinoSerial'):
            try:
                self.arduinoSerial.write(bytes(self.command, 'utf-8'))
                time.sleep(0.05)
            except:
                print("Cannot sending data")
                return
            
            try:
                data = self.arduinoSerial.readlines()
                for line in data:
                    line = line.decode("utf-8")
                    print(line, end="")
                
                if (self.command == "!save#"):
                    time.sleep(2)
                    data = self.arduinoSerial.readlines()
                    for line in data:
                        line = line.decode("utf-8")
                        print(line, end="")

            except:
                print("Cannot get data")
        else:
            print("Port disconnected")
    
    def connect(self, port, baudrate, timeout):
        try:
            self.arduinoSerial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
            print("OK")
        except:
            print("Port cannot open!!")