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


if __name__ == '__main__':
    Apx = TopicApp()