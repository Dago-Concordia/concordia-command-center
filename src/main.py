# Importing Libraries
from tkinter import *
from components.Arduino import Arduino

from components.OffCommandFrame import OffCommandFrame
from components.ManualCommandFrame import ManualCommandFrame
from components.WriteCommandFrame import WriteCommandFrame
from components.GeneralCommandFrame import GeneralCommandFrame
from components.ConnectionFrame import ConnectionFrame

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Concordia Command Center")
        # self.geometry("1024x768")
        self.resizable(False, False)
        # self.iconbitmap(r'img/dago_concordia.ico')
        self.config(bg='gray35')

        colorEven = 'gray35'
        colorOdd = 'gray45'

        self.arduino = Arduino()

        self.container = Frame(self, bd=5, bg='gray35')
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.connectionFrame = ConnectionFrame(self.container, self, color=colorOdd)
        self.connectionFrame.gridMain(row=0, column=0, pady=(10,10), sticky='nswe')

        self.generalCommandFrame = GeneralCommandFrame(self.container, self, color=colorEven)
        self.generalCommandFrame.gridMain(row=1, column=0, pady=(10, 10), sticky = 'nswe')

        self.offCommandFrame = OffCommandFrame(self.container, self, color=colorOdd)
        self.offCommandFrame.gridMain(row=2, column=0, pady=(10, 10), sticky = 'nswe')
        
        self.writeCommandFrame = WriteCommandFrame(self.container, self, colorEven)
        self.writeCommandFrame.gridMain(row=3, column=0, pady=(10, 10), sticky = 'nswe')

        self.manualCommandFrame = ManualCommandFrame(self.container, self, color=colorOdd)
        self.manualCommandFrame.gridMain(row=4, column=0, columnspan=2, pady=(10, 10), sticky = 'nswe')


    def sendToArduino(self, cmd):
        self.arduino.sendCommand(cmd)
    
    def connectToArduino(self, port):
        self.arduino.connect(port, 115200, .1)

    def window_closed(self):
        print("Window closed")
        self.arduino.stop_read_thread()
        self.destroy()


if __name__ == "__main__":
    app = MainWindow()
    app.protocol("WM_DELETE_WINDOW", app.window_closed)
    app.mainloop()
