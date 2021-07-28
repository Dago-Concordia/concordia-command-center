from tkinter import *
from tkinter import ttk


class GeneralCommandFrame(Frame):
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
        self.defButton = Button(self, text="DEF", font = "Helvetica 10 bold", width=10, height=2, command=self.defCommand)
        self.defButton.grid(row=0, column=0, padx=(5, 5), pady=(10, 10))


        # PLAY COMMAND
        self.playButton = Button(self, text="PLAY", bg="lightgreen", font = "Helvetica 10 bold", width=10, height=2, command=self.playCommand)
        self.playButton.grid(row=0, column=1, padx=(5, 30), pady=(10, 10))
        
        self.PLAYIDNUM = 2
        self.playVars = [StringVar() for i in range(self.PLAYIDNUM)]
        self.playEntrys = [Entry(self, width=3, font = "Helvetica 14 bold", textvariable=self.playVars[i]) for i in range(self.PLAYIDNUM)]
        for i in range(self.PLAYIDNUM):
            self.playEntrys[i].grid(row=0, column=i+2, padx=(30, 30), pady=(10, 10))

        for i in range(self.PLAYIDNUM):
            self.playEntrys[i].bind('<Return>', self.playCommandEnter)


        self.labelTextPage = Label(self, text="Page : ", font = "Helvetica 14", bg='lightblue')
        self.labelTextPage.grid(row=1, column=0, padx=(5, 0), pady=(10, 10))

        self.pageOption = [str(i) for i in range(76)] 
        self.pageOptionCombo = ttk.Combobox(self, values=self.pageOption, state="readonly", font = "Helvetica 12 bold", width=6)
        self.pageOptionCombo.grid(row=1, column=1, padx=(5, 0), pady=(10, 10))

        self.labelTextStep = Label(self, text="Step : ", font = "Helvetica 14", bg='lightblue')
        self.labelTextStep.grid(row=1, column=2, padx=(5, 0), pady=(10, 10))

        self.stepOption = [str(i+1) for i in range(20)] 
        self.stepOptionCombo = ttk.Combobox(self, values=self.stepOption, state="readonly", font = "Helvetica 12 bold", width=6)
        self.stepOptionCombo.grid(row=1, column=3, padx=(5, 0), pady=(10, 10))

        self.pageOptionCombo.bind("<<ComboboxSelected>>", self.pageSelected)
        self.stepOptionCombo.bind("<<ComboboxSelected>>", self.stepSelected)
        
        self.gButton = Button(self, text="G",width=10, height=2, font = "Helvetica 10 bold", command=self.gCommand)
        self.gButton.grid(row=2, column=0, padx=(5, 0), pady=(10, 10))


        self.prevButton = Button(self, text="<<",width=10, height=2, font = "Helvetica 10 bold", command=self.prevCommand)
        self.prevButton.grid(row=2, column=1, padx=(5, 0), pady=(10, 10))
        self.nextButton = Button(self, text=">>",width=10, height=2, font = "Helvetica 10 bold", command=self.nextCommand)
        self.nextButton.grid(row=2, column=2, padx=(5, 5), pady=(10, 10))

    def defCommand(self):
        cmd = "!def#"
        print(cmd)
        self.ct.sendToArduino(cmd)
    
    def playCommandEnter(self, event):
        self.playCommand()
    
    def playCommand(self):
        playId = [self.playEntrys[i].get() for i in range(self.PLAYIDNUM)]
        
        param = []
        for i in range(len(playId)):
            id = playId[i]
            if (id != ''):
                try:
                    int(id)
                    param.append(id)
                except:
                    print("ID is not Number")

        if (len(param) == 2):
            if (int(param[0]) > int(param[1])):
                print("Input Invalid")
            else:
                cmd = "!play " + param[0] + " " + param[1] + "#"
                print(cmd)
                # sending cmd to arduino via port
                self.ct.sendToArduino(cmd)
        elif (len(param) == 0):
            cmd = "!play#"
            print(cmd)
            self.ct.sendToArduino(cmd)
        else:
            print("Python: Invalid input")

        # Reset Entry
        for var in self.playVars:
            var.set('')
        self.playEntrys[0].focus_set()
        
    def prevCommand(self):
        # print("prev step")
        stepNum = self.stepOptionCombo.get()
        if (stepNum != ''):
            stepNum = int(stepNum) - 1
            if (stepNum >= 0):
                self.stepOptionCombo.set(str(stepNum))
                self.gCommand()
            else:
                print("Step limit")
        else:
            print("Select step first")
    
    def nextCommand(self):
        # print("next step")
        stepNum = self.stepOptionCombo.get()
        if (stepNum != ''):
            stepNum = int(stepNum) + 1
            if (stepNum <= 20):
                self.stepOptionCombo.set(str(stepNum))
                self.gCommand()
            else:
                print("Step limit")
        else:
            print("Select step first")

    def gCommand(self):
        stepNum = self.stepOptionCombo.get()
        if (self.pageOptionCombo.get() != ''):
            if (stepNum == ''):
                self.stepOptionCombo.set('1')
                stepNum = '1'
            cmd = "!g " + stepNum + "#"
            print(cmd)
            self.ct.sendToArduino(cmd)

    def pageSelected(self, event):
        pageNum = self.pageOptionCombo.get()
        cmd = "!p " + pageNum + "#"
        print(cmd)
        # Send command to arduino
        self.ct.sendToArduino(cmd)

        # Reset Step Selection
        self.stepOptionCombo.set('')

    def stepSelected(self, event):
        stepNum = self.stepOptionCombo.get()
        cmd = "!g " + stepNum + "#"
        print(cmd)

        # Send command to Arduino
        self.ct.sendToArduino(cmd)
    
    def gridMain(self, **kwargs): ######## grid -> grid_
        self.mainFrame.grid(**kwargs)
    
    def gridMain_forget(self):
        self.mainFrame.grid_forget()

    def placeMain(self, **kwargs):
        self.mainFrame.place(**kwargs)

    