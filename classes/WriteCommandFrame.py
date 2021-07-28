from ast import Param
from tkinter import *
from tkinter import ttk


class WriteCommandFrame(Frame):
    def __init__(self, master, controller, color):
        self.WIDTH = 512
        self.HEIGHT = 384

        self.ct = controller
        # color = "gray35"

        self.mainFrame = Frame(master, bg=color)
        Frame.__init__(self, self.mainFrame, width=self.WIDTH, height=self.HEIGHT, background=color)
        self.grid(row=0, column=0)

        self.initWidget()
    
    def initWidget(self):
        # get
        self.getButton = Button(self, text="GET", font = "Helvetica 10 bold", width=10, height=2, bg='lightblue', command=self.getCommand)
        self.getButton.grid(row=0, column=0, padx=(5, 30), pady=(10, 10))

        # SAVE
        self.saveButton = Button(self, text="SAVE", font = "Helvetica 10 bold", width=10, height=2, bg='lightgreen', command=self.saveCommand)
        self.saveButton.grid(row=0, column=1, padx=(30, 5), pady=(10, 10))

        # WRITE STEP COMMAND
        self.writeStepButton = Button(self, text="WRITE STEP", font = "Helvetica 10 bold", width=10, height=2, command=self.writeStepCommand)
        self.writeStepButton.grid(row=1, column=0, padx=(5, 5), pady=(10, 10))

        self.writeStepCommadOption = ["w", "wh", "wa", "wra", "wla", "whip", "wf", "wrf", "wlf"]
        self.writeStepCommanOptionCombo = ttk.Combobox(self, values=self.writeStepCommadOption, state="readonly", font = "Helvetica 12 bold", width=7)
        self.writeStepCommanOptionCombo.grid(row=1, column=1, padx=(0, 5), pady=(10, 10))

        self.WRITESTEPNUM = 4
        self.writeStepVars = [StringVar() for i in range(self.WRITESTEPNUM)]
        self.writeStepEntrys = [Entry(self, width=3, font = "Helvetica 14 bold", textvariable=self.writeStepVars[i]) for i in range(self.WRITESTEPNUM)]
        for i in range(self.WRITESTEPNUM):
            self.writeStepEntrys[i].grid(row=1, column=i+2, padx=(10, 10), pady=(10, 10))
        
        for i in range(self.WRITESTEPNUM):
            self.writeStepEntrys[i].bind('<Return>', self.writeStepCommandEnter)
        

        # WRITE PAGE COMMAND
        self.writePageButton = Button(self, text="WRITE PAGE", font = "Helvetica 10 bold", width=10, height=2, command=self.writePageCommand)
        self.writePageButton.grid(row=2, column=0, padx=(5, 5), pady=(10, 10))

        self.writePageCommadOption = ["wBP", "wBPra", "wBPla", "wBPhip", "wBPf", "wBPrf", "wBPlf"]
        self.writePageCommanOptionCombo = ttk.Combobox(self, values=self.writePageCommadOption, state="readonly", font = "Helvetica 12 bold", width=7)
        self.writePageCommanOptionCombo.grid(row=2, column=1, padx=(0, 5), pady=(10, 10))

        self.WRITEPAGENUM = 4
        self.writePageVars = [StringVar() for i in range(self.WRITEPAGENUM)]
        self.writePageEntrys = [Entry(self, width=3, font = "Helvetica 14 bold", textvariable=self.writePageVars[i]) for i in range(self.WRITEPAGENUM)]
        for i in range(self.WRITEPAGENUM):
            self.writePageEntrys[i].grid(row=2, column=i+2, padx=(10, 10), pady=(10, 10))
        
        for i in range(self.WRITEPAGENUM):
            self.writePageEntrys[i].bind('<Return>', self.writePageCommandEnter)
        
    
    def getCommand(self):
        cmd = "!get#"
        print(cmd)
        self.ct.sendToArduino(cmd)

    def saveCommand(self):
        cmd = "!save#"
        print(cmd)
        self.ct.sendToArduino(cmd)

    def writeStepCommandEnter(self, event):
        self.writeStepCommand()
    
    def writePageCommandEnter(self, event):
        self.writePageCommand()

    def writeStepCommand(self):
        cmd = self.writeStepCommanOptionCombo.get()
        if (cmd != ""):
            args = [self.writeStepVars[i].get() for i in range(self.WRITESTEPNUM)]
            param = ""
            for arg in args:
                if (arg != ""):
                    try:
                        int(arg)
                        param += arg
                        param += " "
                    except:
                        print("Not a number")
            
            if (param != ""):
                param = param[:len(param)-1]
                cmd = "!" + cmd + " " + param + "#"
                print(cmd)
                # Send COmmand To Arduino
                self.ct.sendToArduino(cmd)
            else:
                print("Invalid input")
            
            # reset var
            for var in self.writeStepVars:
                var.set('')
            self.writeStepEntrys[0].focus_set()
        else:
            print("Command is not selected!")

    def writePageCommand(self):
        cmd = self.writePageCommanOptionCombo.get()
        if (cmd != ""):
            args = [self.writePageVars[i].get() for i in range(self.WRITEPAGENUM)]
            param = ""
            for arg in args:
                if (arg != ""):
                    try:
                        int(arg)
                        param += arg
                        param += " "
                    except:
                        print("Not a number")
            
            if (param != ""):
                param = param[:len(param)-1]
                cmd = "!" + cmd + " " + param + "#"
                print(cmd)
                # Send COmmand To Arduino
                self.ct.sendToArduino(cmd)
            else:
                print("Invalid input")
            
            # reset var
            for var in self.writePageVars:
                var.set('')
            self.writePageEntrys[0].focus_set()
        else:
            print("Command is not selected!")
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    