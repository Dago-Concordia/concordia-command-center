import serial
import time
from threading import *

class Arduino:
    def __init__(self):
        self.command = "!def#"

        self.read_thread_indicator = False
    
    def sendCommand(self, cmd):
        # cmd = "!help#"
        self.command = cmd
        Thread(target=self.write_data).start()

    def write_data(self):
        if hasattr(self, 'arduinoSerial'):
            try:
                self.arduinoSerial.write(bytes(self.command, 'utf-8'))
                time.sleep(0.05)
            except:
                print("Cannot sending data")
                return
        else:
            print("Port disconnected")
    
    def connect(self, port, baudrate, timeout):
        try:
            self.arduinoSerial = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
            print("OK")
            Thread(target=self.read_data).start()
        except:
            print("Port cannot open!!")
    
    def read_data(self):
        if hasattr(self, 'arduinoSerial'):
            print("Ready to get data")
            try:
                while (True):
                    if (self.arduinoSerial.in_waiting > 0):
                        data = self.arduinoSerial.readlines()
                        for line in data:
                            line = line.decode("utf-8")
                            print(line, end="")
                    
                    if (self.read_thread_indicator):
                        break
                        
                    time.sleep(0.01)
            
            except Exception as e:
                print("Cannot get data : ", end="")
                print(e)
        else:
            print("Port disconnected")
    
    def stop_read_thread(self):
        self.read_thread_indicator = True