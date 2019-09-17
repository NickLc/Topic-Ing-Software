import tkinter as tk

#@Class Abstract
class DoorState:
    def __init__(self):
        self.name = 'Abstrac State'
    def open(self):
        pass
    def close(self):
        pass
    def arm(self):
        pass
    def disarm(self):
        pass
    def repair(self):
        pass
    def test(self):
        pass
    def endTest(self):
        pass

class Open(DoorState):
    def __init__(self):
        self.name = 'Open State'
    def open(self):
        return Open()
    def close(self):
        return Close()
    def arm(self):
        return Open()
    def disarm(self):
        return Open()
    def repair(self):
        return Open()
    def test(self):
        return Open()
    def endTest(self):
        return Open()

class Close(DoorState):
    def __init__(self):
        self.name = 'Close State'     
    def open(self):
        return Open()
    def close(self):
        return Close()
    def arm(self):
        return Arm()
    def disarm(self):
        return Close()
    def repair(self):
        return Close()
    def test(self):
        return Test()
    def endTest(self):
        return Close()

class Arm(DoorState):
    def __init__(self):
        self.name = 'Arm State'
    def open(self):
        return Emergency()  
    def close(self):
        return Arm()
    def arm(self):
        return Arm()
    def disarm(self):
        return Close()
    def repair(self):
        return Arm()
    def  test(self):
        return Arm()
    def endTest(self):
        return Arm()
        
class Emergency(DoorState):
    def __init__(self):
        self.name = 'Emergency State'
    def open(self):
        return Emergency()
    def close(self):
        return Emergency()
    def arm(self):
        return Emergency()
    def disarm(self):
        return Emergency()
    def repair(self):
        return Close()
    def  test(self):
        return Emergency()
    def endTest(self):
        return Emergency()
        
class Test(DoorState):
    def __init__(self):
        self.name = 'Test State'
    def open(self):
        return Test()
    def close(self):
        return Test()
    def arm(self):
        return Test()
    def disarm(self):
        return Test()
    def repair(self):
        return Test()
    def test(self):
        return Test()
    def endTest(self):
        return Close()

class Door:
    def __init__(self, state):
        self.state = state
    def open(self):
        self.state = self.state.open()
    def close(self):
        self.state = self.state.close()
    def arm(self):
        self.state = self.state.arm()
    def disarm(self):
        self.state = self.state.disarm()
    def repair(self):
        self.state = self.state.repair()
    def test(self):
        self.state = self.state.test()
    def endTest(self):
        self.state = self.state.endTest()

class TopicApp():
    def __init__(self):
        
        self.door = Door(Close())

        self.mainWindow = tk.Tk()
        self.mainWindow.title("Welcome App Descount")
        self.mainWindow.geometry('300x200')

        self.lbl_titleState = tk.Label(self.mainWindow, text='State:')
        self.lbl_titleState.grid(column=0, row=0, padx=5, pady=5)
        
        self.lbl_showState = tk.Label(self.mainWindow, text=self.door.state.name)
        self.lbl_showState.grid(column=0, row=1, padx=1, pady=1)

        self.btn_Open = tk.Button(self.mainWindow, text='Open', 
                    command = lambda : self.open())
        self.btn_Open.grid(column=1, row=2, padx=20)

        self.btn_Close = tk.Button(self.mainWindow, text='Close', 
                    command = lambda : self.close())
        self.btn_Close.grid(column=1, row=3,padx=20)
        
        self.btn_Arm = tk.Button(self.mainWindow, text='Arm', 
                    command = lambda : self.arm())
        self.btn_Arm.grid(column=1, row=4)
        
        self.btn_Disarm = tk.Button(self.mainWindow, text='Disarm', 
                    command = lambda : self.disarm())
        self.btn_Disarm.grid(column=1, row=5)
        
        self.btn_Repair = tk.Button(self.mainWindow, text='Repair', 
                    command = lambda : self.repair())
        self.btn_Repair.grid(column=1, row=6)

        self.btn_Test = tk.Button(self.mainWindow, text='Test', 
                    command = lambda : self.test())
        self.btn_Test.grid(column=2, row=2)

        self.btn_EndTest = tk.Button(self.mainWindow, text='EndTest', 
                    command = lambda : self.endTest())
        self.btn_EndTest.grid(column=2, row=3)

        self.mainWindow.mainloop()

    def open(self):
        self.door.open()
        self.lbl_showState.configure(text=self.door.state.name)

    def close(self):
        self.door.close()
        self.lbl_showState.configure(text=self.door.state.name)

    def arm(self):
        self.door.arm()
        self.lbl_showState.configure(text=self.door.state.name)

    def disarm(self):
        self.door.disarm()
        self.lbl_showState.configure(text=self.door.state.name)

    def repair(self):
        self.door.repair()
        self.lbl_showState.configure(text=self.door.state.name)
    
    def test(self):
        self.door.test()
        self.lbl_showState.configure(text=self.door.state.name)
    
    def endTest(self):
        self.door.endTest()
        self.lbl_showState.configure(text=self.door.state.name)
    
if __name__ == '__main__':
    Apx = TopicApp()