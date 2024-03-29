from tkinter import *

class Memento():
    def __init__(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
        
class Caretaker():

    def __init__(self, mementos):
        """Input: list of mements"""

        self.mementos = mementos

    def _push_(self,memento):
        self.mementos.append(memento)

    def _pop_(self):
        last_memento = self.mementos[-1]
        self.mementos.pop()
        return last_memento

class TopicApp():
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Topicos Software")
        self.window.geometry('350x200')
        self.window.config(bg="#00FF00")

        self.caretakerZ = Caretaker([Memento("#00FF00")])
        self.caretakerY = Caretaker([])

        btn_blue = Button(self.window, text="Blue", command = lambda : self.__change_color("#0000FF"))
        btn_blue.grid(column=0, row=0)

        btn_red = Button(self.window, text="Red", command = lambda : self.__change_color("#FF0000"))
        btn_red.grid(column=0, row=1)

        btn_green = Button(self.window, text="Green", command = lambda : self.__change_color("#00FF00"))
        btn_green.grid(column=0, row=2)

        btn_ctr_z = Button(self.window, text="Crt-z", command = lambda : self.__restore_memento())
        btn_ctr_z.grid(column=0, row=3)

        btn_ctr_y = Button(self.window, text="Crt-y", command = lambda : self.__adelant_memento())
        btn_ctr_y.grid(column=0, row=4)
        
        self.window.mainloop()


    def __change_color(self, color):
        self.window.config(bg=color)
        self.caretakerZ._push_(Memento(color))
        self.caretakerY = Caretaker([])
    
    def __restore_memento(self):
        memento = self.caretakerZ._pop_()
        self.caretakerY._push_(memento)
        self.window.config(bg=memento.get_color())

    def __adelant_memento(self):
        memento = self.caretakerY._pop_()
        self.caretakerZ._push_(memento)
        self.window.config(bg=memento.get_color())
        
if __name__=='__main__':
    Apx = TopicApp()