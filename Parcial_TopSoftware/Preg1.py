import tkinter as tk
from tkinter import *

class Alumno():
    def __init__(self, sexo, nivel):
        self.sexo = sexo
        self.nivel = nivel

class Handler():
    """
    The Handler interfae declares a method for building the
    chain of handlers. It also declarate a method for executing a request
    """

    #@abstractmethod
    def set_next(self, handler):
        pass
    
    #@abstractmethod
    def handle(self, request: Alumno):
        pass

class AbstractHandler(Handler):
    """
    Ther default chaining behovior can be implement inside a base handler
    class.
    """
    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request: Alumno):
        if self._next_handler:
            return self._next_handler.handle(request)
        
        return None

"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""

class HNivel1(AbstractHandler):
    def handle(self, request: Alumno):
        """Recibe el sexo del alumno y retorna un paquete de promocion"""
        if request.nivel == '1':
            if request.sexo=='V':
                return 'Zapatillas, buzo, soga de saltar'
            elif request.sexo=='M':
                return 'Zapatillas, buzo, 6 m de elástico'
        else:
            print("Pasando a Nivel 2")
            return super().handle(request)

class HNivel2(AbstractHandler):
    def handle(self, request: Alumno):
        """Recibe el sexo del alumno y retorna un paquete de promocion"""
        if request.nivel == '2':
            if request.sexo=='V':
                return 'Zapatillas, buzo, pelota de fútbol Nro. 4'
            elif request.sexo=='M':
                return 'Zapatillas, buzo, pelota de voléybol Nro. 4'
        else:
            print("Pasando a Nivel 3")
            return super().handle(request)

class HNivel3(AbstractHandler):
    def handle(self, request: Alumno):
        """Recibe el sexo del alumno y retorna un paquete de promocion"""
        if request.nivel == '3':
            if request.sexo=='V':
                return 'Bate, pelota, guante'
            elif request.sexo=='M':
                return 'Bate, pelota, guante'
        else:
            print("Pasando a Nivel 4")
            return super().handle(request)

class HNivel4(AbstractHandler):
    def handle(self, request: Alumno):
        """Recibe el sexo del alumno y retorna un paquete de promocion"""
        if request.nivel == '4':
            if request.sexo=='V':
                return 'Ropa de baño, gorro, goggles, chimpunes'
            elif request.sexo=='M':
                return 'Ropa de baño, gorro, goggles, tutú'
        else:
            print("Pasando a Nivel 5")
            return super().handle(request)

class HNivel5(AbstractHandler):
    def handle(self, request: Alumno):
        """Recibe el sexo del alumno y retorna un paquete de promocion"""
        if request.nivel == '5':
            if request.sexo=='V':
                return 'Ropa de baño, gorro, goggles, chimpunes, skateboard'
            elif request.sexo=='M':
                return 'Ropa de baño, gorro, goggles, stepper'
        else:
            return super().handle(request)

class HNivel6(AbstractHandler):
    def handle(self, request: Alumno):
        """Recibe el sexo del alumno y retorna un paquete de promocion"""
        return 'maximo nivel'



class AppDescuentos():
    def __init__(self):

        self.mainWindow = tk.Tk()
        self.mainWindow.title("Welcome App Descount")
        self.mainWindow.geometry('450x200')


        self.dataFrame = tk.Frame(self.mainWindow)
        
        self.lbl_sexo = tk.Label(self.mainWindow, text='Sexo:[V,M]')
        self.lbl_sexo.grid(column=0, row=0, padx=20, pady=3)
        self.inp_sexo = tk.Entry(self.mainWindow, width=8)
        self.inp_sexo.grid(column=0, row=1, padx=20, pady=5)
        
        self.lbl_nivel = tk.Label(self.mainWindow, text='Nivel:[1-5]')
        self.lbl_nivel.grid(column=1, row=0)
        self.inp_nivel = tk.Entry(self.mainWindow, width=8)
        self.inp_nivel.grid(column=1, row=1, pady=6)
    
        self.btn_create = tk.Button(self.mainWindow, text='Get Lista', 
                    command = lambda : self.get_Lista()).grid(column=2, row=2)

        self.lbl_Result = tk.Label(self.mainWindow, text='----')
        self.lbl_Result.grid(column=0, row=2, padx=8)

        self.mainWindow.mainloop()

    def get_Lista(self):
        sexo = self.inp_sexo.get()
        nivel = self.inp_nivel.get()
        alumno = Alumno(sexo, nivel)

        N1,N2,N3,N4,N5 = HNivel1(), HNivel2(), HNivel3(), HNivel4(), HNivel5()
        N1.set_next(N2)
        N2.set_next(N3)
        N3.set_next(N4)
        N4.set_next(N5)
        N5.set_next(HNivel6())

        resl_list = N1.handle(alumno)
        self.lbl_Result.configure(text=resl_list)


if __name__ == "__main__":
    app = AppDescuentos()