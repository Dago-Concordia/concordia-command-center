from tkinter import *

class ManualCommandFrame(Frame):
    def __init__(self, master, controller, color):
        self.WIDTH = 900
        self.HEIGHT = 50

        self.ct = controller
        # color = "gray35"

        self.mainFrame = Frame(master, bg=color)
        Frame.__init__(self, self.mainFrame, width=self.WIDTH, height=self.HEIGHT, background=color)
        self.grid(row=0, column=0)

        self.initWidget()
    
    def initWidget(self):
        self.cmdVar = StringVar()
        self.commandEntry = Entry(self, width=40, textvariable=self.cmdVar, font = "Helvetica 14 bold")
        self.commandEntry.grid(row=0, column=0, padx=(5, 5))
        self.commandEntry.bind('<Return>', self.sendCommandEnter)


        self.sendButton = Button(self, text="Send", width=7, command=self.sendCommand)
        self.sendButton.grid(row=0, column=1)
        
    def sendCommand(self):
        cmd = self.cmdVar.get()
        self.cmdVar.set("")
        if (cmd != ""):
            finalCommand = ("!"+cmd+"#")
            print(finalCommand)
            self.ct.sendToArduino(finalCommand)
    
    def sendCommandEnter(self, event):
        self.sendCommand()

        
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    