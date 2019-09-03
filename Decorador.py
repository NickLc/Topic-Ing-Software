from tkinter import *
class Pizza():
    def __init__(self, precio):
        self.precio = precio
    
    def get_precio(self):
        pass

class BaseJamon(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
        self.pizza.precio += 10
        Pizza.__init__(self, self.pizza.precio)
    
    def get_precio(self):
        return self.pizza.precio
#@Class Abstract
class AbstractDecorator(Pizza):
    def __init__(self, pizza):
        Pizza.__init__(self, pizza.get_precio())
        self.precio =  pizza.get_precio()

    def get_precio(self):
        pass

class Chorizo(AbstractDecorator):
    def __init__(self, pizza):
        pizza.precio = pizza.get_precio() + 2
        self.pizza = pizza
        AbstractDecorator.__init__(self, self.pizza)

    def get_precio(self):
        return self.pizza.precio

class Jalapeno(AbstractDecorator):
    def __init__(self, pizza):
        pizza.precio = pizza.get_precio() + 4
        self.pizza = pizza
        AbstractDecorator.__init__(self, self.pizza)

    def get_precio(self):
        return self.pizza.precio


class TopicApp():
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Topicos Software")
        self.window.geometry('120x150')
        self.window.config(bg="#00FF00")
        
        self.pizza = Pizza(0)
        self.pizza = BaseJamon(self.pizza)
        
        self.btn_chorizo = Button(self.window, text="Chorizo", command = lambda : self.add_chorizo())
        self.btn_chorizo.grid(column=0, row=0)

        self.btn_jalapeno = Button(self.window, text="Jalapeno", command = lambda : self.add_jalapeno())
        self.btn_jalapeno.grid(column=0, row=1)

        self.btn_Xqueso = Button(self.window, text="Xqueso")
        self.btn_Xqueso.grid(column=0, row=2)

        self.btn_peperoni = Button(self.window, text="Peperoni")
        self.btn_peperoni.grid(column=0, row=3)

        self.btn_pina = Button(self.window, text="Piña")
        self.btn_pina.grid(column=0, row=4)

        self.btn_crear = Button(self.window, text="Crear", command = lambda : self.create_Pizza())
        self.btn_chorizo.grid(column=0, row=0)
        self.btn_crear.grid(column=1, row=1)

        self.lb_precio = Label(self.window, text="Precio")
        self.lb_precio.grid(column=1, row=2)

        self.lb_result = Label(self.window, text=self.pizza.get_precio())
        self.lb_result.grid(column=2, row=2)  
        
        self.window.mainloop()

    def add_chorizo(self):
        self.pizza = Chorizo(self.pizza)
        print("Chorizo agregado..   precio:{}\n".format(self.pizza.get_precio()))

    def add_jalapeno(self):
        self.pizza = Jalapeno(self.pizza)
        print("jalapeno agregado..   precio:{}\n".format(self.pizza.get_precio()))
    

    def create_Pizza(self):
        self.lb_result.configure(text=str(self.pizza.get_precio()))

if __name__ == '__main__':
    Apx = TopicApp()