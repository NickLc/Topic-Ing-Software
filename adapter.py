import tkinter as tk
from tkinter import messagebox
class Vector():
    def __init__(self, vector: list):
        self.vectorData = vector

    def getV(self, pos):
        return self.vectorData[pos] 

    def setV(self, pos, value):
        self.vectorData[pos] = value

class AbstractAdapter():
    def __init__(self, fil, col):
        self.filas = fil
        self.col = col

    def getElement(self, posf, posc):
        pass

    def setElement(self, posf, posc, value):
        pass

class Adapter(AbstractAdapter):
    def __init__(self, fil, col, vector:list):
        self.fil = fil
        self.col = col
        AbstractAdapter.__init__(self, fil, col)
        self.matrix = vector

    def getElement(self, posf, posc):
        return self.matrix[(posf-1)*self.col + (posc-1)]

    def setElement(self, posf, posc, value):
        self.matrix[(posf-1)*self.col + (posc-1)] = value


class TopicApp():
    def __init__(self):

        #Datos del adaptador
        vector = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.m, self.n = 3 , 4
        self.adapter = Adapter(self.m, self.n,vector)

        self.mainWindow = tk.Tk()
        self.mainWindow.title("Welcome App Descount")
        self.mainWindow.geometry('200x100')

        self.lbl_x = tk.Label(self.mainWindow, text='row:')
        self.lbl_x.grid(column=0, row=0, padx=20, pady=3)
        self.inp_x = tk.Entry(self.mainWindow, width=8)
        self.inp_x.grid(column=0, row=1, padx=20, pady=5)
        
        self.lbl_y = tk.Label(self.mainWindow, text='column: ')
        self.lbl_y.grid(column=1, row=0)
        self.inp_y = tk.Entry(self.mainWindow, width=8)
        self.inp_y.grid(column=1, row=1, pady=6)
    
        self.btn_create = tk.Button(self.mainWindow, text='Get', 
                    command = lambda : self.get_Matrix()).grid(column=2, row=2)

        self.lbl_Result = tk.Label(self.mainWindow, text='----')
        self.lbl_Result.grid(column=0, row=2, padx=8)
        
        self.mainWindow.mainloop()

    def get_Matrix(self):
        fil = int(self.inp_x.get())
        col = int(self.inp_y.get())

        #Mensajes de error en caso de superar el rango de la matrix
        if(fil < 1 or fil > self.m):
            messagebox.showerror('Error', 'index row incorrect') 
        
        if(col < 1 or col > self.n):
            messagebox.showerror('Error', 'index column incorrect') 
        
        result = self.adapter.getElement(fil, col)
        self.lbl_Result.configure(text=str(result))
        
if __name__ == '__main__':
    Apx = TopicApp()