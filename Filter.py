import tkinter as tk
from tkinter import scrolledtext
import re
#@Class Abstract
class AbstractFilter:
    def to_Filter(self):
        pass

class FilterSpace(AbstractFilter):

    def to_Filter(self, cad):
        """ Filter all space and tab from text input """
        cad_output = re.sub(r'[\t ]+'," ", cad, re.M)
        return cad_output
class FilterWord(AbstractFilter):

    def to_Filter(self, cad):
        lst = re.findall(r'[\w]+', cad, re.M)
        cad_output = "\n".join(lst)
        return cad_output


class TopicApp:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Regular Expresion")
        self.window.geometry('680x400')
        self.window.config(bg="#FFFFFF")
        
        self.cad_input = " "
        self.cad_output = " "
        self.regex = re.compile(r' ', re.M)

        lbl_input = tk.Label(self.window, text='Texto')
        lbl_input.grid(column =0, row=2, sticky='W',padx=10)

        self.scroll_input = tk.scrolledtext.ScrolledText(self.window,width=40,height=10)
        self.scroll_input.grid(column=0,row=3, sticky='W',padx=10)

        lbl_output = tk.Label(self.window, text='Texto output')
        lbl_output.grid(column =0, row=4, sticky='W',padx=10)

        self.scroll_output = scrolledtext.ScrolledText(self.window,width=40,height=10)
        self.scroll_output.grid(column=0,row=5, sticky='W',padx=10)
  
        ## ----------B U T T O N --------------------
        buton_filSpace = tk.Button(self.window, text='filSpace', command = self.filSpace)
        buton_filSpace.grid(column=2, row=3, sticky='W',padx=10)

        buton_filWord = tk.Button(self.window, text='filWord', command = self.filWord)
        buton_filWord.grid(column=2, row=4, sticky='W',padx=10)
        
        self.window.mainloop()
    
    def getInput(self):

        self.scroll_output.delete(0.0, tk.END)
        cad = self.scroll_input.get("0.0", tk.END)
        return cad

    def setOutput(self, cad):
        self.scroll_output.insert(tk.INSERT, cad)

    def filSpace(self):
        """ Filter all space and tab from text input """

        cad = FilterSpace().to_Filter(self.getInput())
        self.setOutput(cad)
    
    def filWord(self):
        """Filter all word from text input"""
        cad = FilterWord().to_Filter(self.getInput())
        self.setOutput(cad)
        

if __name__=='__main__':
    Apx = TopicApp()