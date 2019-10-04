import tkinter as tk
from tkinter import scrolledtext
import re

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
        buton_filter_space = tk.Button(self.window, text='filter_space', command = self.filter_Space)
        buton_filter_space.grid(column=2, row=3, sticky='W',padx=10)

        buton_filter_word = tk.Button(self.window, text='filter_word', command = self.filter_Word)
        buton_filter_word.grid(column=2, row=4, sticky='W',padx=10)
        
        self.window.mainloop()
    
    def get_input(self):

        self.scroll_output.delete(0.0, tk.END)
        cad = self.scroll_input.get("0.0", tk.END)
        return cad

    def set_output(self, cad):
        self.scroll_output.insert(tk.INSERT, cad)

    def filter_Space(self):
        """ Filter all space and tab from text input """
        self.regex = re.compile(r'[\t ]+', re.M)
        cad_output = self.regex.sub(" ", self.get_input())
        self.set_output(cad_output)
    
    def filter_Word(self):
        """Filter all word from text input"""
        self.regex = re.compile(r'[\w]+', re.M)
        list_output = self.regex.findall(self.get_input())
        tam = len(list_output)
        cad_output = "\n".join(list_output)
        self.set_output(cad_output+"\nMatches: "+ tam)
        

if __name__=='__main__':
    Apx = TopicApp()