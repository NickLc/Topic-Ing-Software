import tkinter as tk
from tkinter import scrolledtext
import re

class TopicApp:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Regular Expresion")
        self.window.geometry('680x500')
        self.window.config(bg="#FFFFFF")
        
        lbl_RE = tk.Label(self.window, text='Regular Expresion')
        lbl_RE.grid(column =0, row=0, sticky='W',padx=10)

        self.entry_RE = tk.Entry(self.window, width=20)
        self.entry_RE.grid(column=0, row=1, sticky='W',padx=10)

        lbl_txt_init = tk.Label(self.window, text='Texto')
        lbl_txt_init.grid(column =0, row=2, sticky='W',padx=10)

        self.scroll_txt_init = tk.scrolledtext.ScrolledText(self.window,width=40,height=10)
        self.scroll_txt_init.grid(column=0,row=3, sticky='W',padx=10)

        lbl_txt_match = tk.Label(self.window, text='Texto Match')
        lbl_txt_match.grid(column =0, row=4, sticky='W',padx=10)

        self.scroll_txt_match = scrolledtext.ScrolledText(self.window,width=20,height=10)
        self.scroll_txt_match.grid(column=0,row=5, sticky='W',padx=10)

        lbl_txt_group = tk.Label(self.window, text='Texto group')
        lbl_txt_group.grid(column =1, row=4, sticky='W')

        self.scroll_txt_group = scrolledtext.ScrolledText(self.window,width=20,height=10)
        self.scroll_txt_group.grid(column=1, row=5, sticky='W')

        buton_match = tk.Button(self.window, text='Match', command = self.clicked)
        buton_match.grid(column=2, row=4, sticky='W',padx=10)

        self.lbl_num_match = tk.Label(self.window, text='# matches: ---')
        self.lbl_num_match.grid(column=2, row=5, sticky='W',padx=10)
        
        self.window.mainloop()

    def clicked(self):
        # Clear buffer
        self.scroll_txt_match.delete(0.0, tk.END)

        cad = self.scroll_txt_init.get("0.0", tk.END)
        lis = cad.split("\n")
        
        matchs = []
        groups = []
        
        # Search all match of txt init
        for let in lis:
            matchs.append(re.findall(self.entry_RE.get(), let))
            groups.append(re.search(self.entry_RE.get(), let))
  
        # Put txt_match into of stroll 
        txt_group = []
        for i in groups:
            if i != None:
                txt_group.append(i.string)

        txt_match = []      
        for i in matchs:
            if i != []:
                txt_match.append(i)

        # Put txt_match into of stroll 
        self.scroll_txt_match.insert(tk.INSERT, txt_match)
        self.scroll_txt_group.insert(tk.INSERT, txt_group)

        # how much match 
        self.lbl_num_match.configure(text='# matches: {}'.format(len(txt_match)))

        

if __name__=='__main__':
    Apx = TopicApp()