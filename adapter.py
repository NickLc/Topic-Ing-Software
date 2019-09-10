import tkinter as tk

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

    def getElement(self, posx, posy):
        pass

    def setElement(self, posx, posy, value):
        pass

class Adapter(AbstractAdapter):
    def __init__(self, fil, col, vector:list):
        self.fil = fil
        self.col = col
        AbstractAdapter.__init__(self, fil, col)
        self.matrix = vector

    def getElement(self, posx, posy):
        return self.matrix[posy*self.fil + posx]

    def setElement(self, posx, posy, value):
        self.matrix[posy*self.fil + posx] = value


class TopicApp():
    def __init__(self):

        #Datos del adaptador
        vector = [1,2,3,5,6,7,9,10,11]
        fil, col = 3 , 4
        self.adapter = Adapter(fil,col,vector)
        print(self.adapter.getElement(0,1))

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
        x = int(self.inp_x.get())
        y = int(self.inp_y.get())
        
        result = self.adapter.getElement(y-1, x-1)
        self.lbl_Result.configure(text=str(result))
        
if __name__ == '__main__':
    Apx = TopicApp()