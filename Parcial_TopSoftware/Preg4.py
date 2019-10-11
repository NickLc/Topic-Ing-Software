import re
import tkinter as tk
from tkinter import scrolledtext

class AbstractFilter:
    def __init__(self):
        pass
    def repl(self):
        pass
    def to_Filter(self):
        pass


class FilReplacePrice(AbstractFilter):
    def __init__(self):
        self.name = 'Filter Replace Price'
    
    def repl(self, m):
        newNum = re.sub(r'[,]', '', m.group(1))

        return 'S/. {0:.3f}'.format(float(newNum)/3.34)

    def to_Filter(self, cad):
        cad_output = re.sub(r'\$\s*([\d\,\.]+)', self.repl, cad)
        return cad_output

class FilGetMount(AbstractFilter):
    def __init__(self):
        self.name = 'Filter amount total for month'

    def to_Filter(self, cad, month):
        amount = 0
        rule = '.*{}:?\s*?S/\.\s*?([\d\,\.]+)'.format(month)
        pattern = re.compile(rule, re.IGNORECASE)

        for m in pattern.finditer(cad):
            newNum = re.sub(r'[,]', '', m.group(1))
            amount += float(newNum)
        return amount


fileSales = open('text_SalesForMonth2.txt', 'r')
cad = fileSales.read()
fileSales.close()

cad = FilReplacePrice().to_Filter(cad)

months = ['Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Octubre','Noviembre','Diciembre']
amount_Mount = {}

for m in months:
    amount = FilGetMount().to_Filter(cad, m)
    amount_Mount.update({m : amount})

print(amount_Mount)




class TopicApp:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Regular Expresion")
        self.window.geometry('650x440')
        self.window.config(bg="#FFFFFF")


        frameFilter = tk.Frame(self.window)

        buton_filGetMount = tk.Button(frameFilter, text='filGetMount', 
                        command = self.filGetMount)
        buton_filGetMount.grid(column=0, row=0, sticky='W',pady=4)
        
        buton_filReplacePrice = tk.Button(frameFilter, text='filReplacePrice', 
                        command = self.filReplacePrice)
        buton_filReplacePrice.grid(column=0, row=1, sticky='W',pady=4)
        
        frameFilter.grid(column=0, row=0)

        frame_input = tk.Frame(self.window)

        lbl_input = tk.Label(frame_input, text='Texto')
        lbl_input.grid(column=0, row=0, sticky='W')

        self.scroll_input = tk.scrolledtext.ScrolledText(frame_input,width=50,height=12)
        self.scroll_input.grid(column=0,row=1, sticky='W')
        frame_input.grid(column=1, row=0)

        frame_output = tk.Frame(self.window)        
        lbl_output = tk.Label(frame_output, text='Texto output')
        lbl_output.grid(column=1, row=5, sticky='W',padx=10)

        self.scroll_output = scrolledtext.ScrolledText(frame_output,width=60,height=12)
        self.scroll_output.grid(column=1,row=6,padx=1)
        frame_output.grid(column=1, row=1)
        
        self.window.mainloop()
    

    def getInput(self):
        self.scroll_output.delete(0.0, tk.END)
        cad = self.scroll_input.get("0.0", tk.END)
        return cad

    def setOutput(self, cad):
        self.scroll_output.insert(tk.INSERT, cad)

    def filGetMount(self):

        """Filter all word from text input"""
        cad = self.getInput()
        cad = FilReplacePrice().to_Filter(cad)

        months = ['Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Octubre','Noviembre','Diciembre']
        cad_new = ''
        for m in months:
            amount = FilGetMount().to_Filter(cad, m)
            cad_new += '{}:\t{}\n'.format(m, amount)

        cad = cad_new

        self.setOutput(cad)
        

    def filReplacePrice(self):
        """Filter all Reverse from text input"""
        cad = self.getInput()
        cad = FilReplacePrice().to_Filter(cad)
        self.setOutput(cad)     

if __name__=='__main__':
    Apx = TopicApp()


