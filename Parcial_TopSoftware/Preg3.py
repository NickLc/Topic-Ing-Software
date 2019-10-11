import tkinter as tk

#@Class Abstract

class DoorState:
    def __init__(self):
        self.name = 'Abstrac State'
    def Apagado(self, temp):
        pass
    def Enfriando(self):
        pass
    def Listo(self):
        pass
    def DetectandoSenal(self):
        pass
    
class Apagado(DoorState):
    def __init__(self):
        self.name = 'Apagado State'
    def Encender(self):
        return DetectandoSenal()
    def Apagar(self, temp):
        return Apagado()
    def SinSenal(self):
        return Apagado()
    def SenalDetectada(self):
        return Apagado()

class Enfriando(DoorState):
    def __init__(self):
        self.name = 'Enfriando State'
    def Encender(self):
        return Enfriando()
    def Apagar(self, temp):
        if temp<50:
            return Apagado()
        else: 
            return Enfriando()
    def SinSenal(self):
        return Enfriando()
    def SenalDetectada(self):
        return Enfriando()

class DetectandoSenal(DoorState):
    def __init__(self):
        self.name = 'Detectando Señal State'
    def Encender(self):
        return DetectandoSenal()
    def Apagar(self,temp):
        return DetectandoSenal()
    def SinSenal(self):
        return DetectandoSenal()
    def SenalDetectada(self):
        return Listo()

class Listo(DoorState):
    def __init__(self):
        self.name = 'Listo State'
    def Encender(self):
        return Listo()
    def Apagar(self,temp):
        if temp > 50:
            return Enfriando()
        else:
            return Apagado()
    def SinSenal(self):
        return DetectandoSenal()
    def SenalDetectada(self):
        return Listo()

class Door:
    def __init__(self, state):
        self.state = state
    def Apagado(self):
        self.state = self.state.Apagado()
    def Enfriando(self):
        self.state = self.state.Enfriando()
    def arm(self):
        self.state = self.state.arm()
    def Listo(self):
        self.state = self.state.Listo()
    def DetectandoSenal(self):
        self.state = self.state.DetectandoSenal()
    def test(self):
        self.state = self.state.test()
    def endTest(self):
        self.state = self.state.endTest()

class TopicApp():
    def __init__(self):
        
        self.door = Door(Enfriando())

        self.mainWindow = tk.Tk()
        self.mainWindow.title("Welcome App Descount")
        self.mainWindow.geometry('300x200')

        self.lbl_titleState = tk.Label(self.mainWindow, text='State:')
        self.lbl_titleState.grid(column=0, row=0, padx=5, pady=5)
        
        self.lbl_showState = tk.Label(self.mainWindow, text=self.door.state.name)
        self.lbl_showState.grid(column=0, row=1, padx=1, pady=1)

        self.btn_Apagado = tk.Button(self.mainWindow, text='Apagado', 
                    command = lambda : self.Apagado())
        self.btn_Apagado.grid(column=1, row=2, padx=20)

        self.btn_Enfriando = tk.Button(self.mainWindow, text='Enfriando', 
                    command = lambda : self.Enfriando())
        self.btn_Enfriando.grid(column=1, row=3,padx=20)
        
        self.btn_Arm = tk.Button(self.mainWindow, text='Arm', 
                    command = lambda : self.arm())
        self.btn_Arm.grid(column=1, row=4)
        
        self.btn_Listo = tk.Button(self.mainWindow, text='Listo', 
                    command = lambda : self.Listo())
        self.btn_Listo.grid(column=1, row=5)
        
        self.btn_DetectandoSenal = tk.Button(self.mainWindow, text='DetectandoSenal', 
                    command = lambda : self.DetectandoSenal())
        self.btn_DetectandoSenal.grid(column=1, row=6)

        self.btn_Test = tk.Button(self.mainWindow, text='Test', 
                    command = lambda : self.test())
        self.btn_Test.grid(column=2, row=2)

        self.btn_EndTest = tk.Button(self.mainWindow, text='EndTest', 
                    command = lambda : self.endTest())
        self.btn_EndTest.grid(column=2, row=3)

        self.mainWindow.mainloop()

    def Apagado(self):
        self.door.Apagado()
        self.lbl_showState.configure(text=self.door.state.name)

    def Enfriando(self):
        self.door.Enfriando()
        self.lbl_showState.configure(text=self.door.state.name)

    def arm(self):
        self.door.arm()
        self.lbl_showState.configure(text=self.door.state.name)

    def Listo(self):
        self.door.Listo()
        self.lbl_showState.configure(text=self.door.state.name)

    def DetectandoSenal(self):
        self.door.DetectandoSenal()
        self.lbl_showState.configure(text=self.door.state.name)
    
    def test(self):
        self.door.test()
        self.lbl_showState.configure(text=self.door.state.name)
    
    def endTest(self):
        self.door.endTest()
        self.lbl_showState.configure(text=self.door.state.name)
    
if __name__ == '__main__':
    Apx = TopicApp()