from tkinter import *
from tkinter import ttk
import lib.widgets as widgets

#Диалоговые окна
class Window(Tk):
    """
    класс окна расчета по одной из двух формул
    """
    def __init__(self, main, id):
        super().__init__()
        #print(id)
        #конфигурация окна
        self.title(f"Розрахунок за формулою {id}")
        self.geometry("800x850")
        self.resizable(False, False)
        self.focus_force()

        #выбор набора парамметров исходя из выбранной формули
        self.id = id
        self.frame = Frame(self, padx=0, pady=0)
        self.frame.pack()

        if self.id == '1':
            self.header = Label(self.frame, text="Кзф = [0,77 Ч К1  Ч К ст  Ч Кп / ((1-Кш) Ч  ((К’о Ч Кст +1) + Кп Ч (Ко Ч К ст +1)) Ч К м)] Ч KНЗ,        (Г.7) ")
            self.header.grid(row=0, column=0, columnspan= 2, ipadx=0, ipady=0, padx=[50, 50], pady=[30, 0])
            [(ttk.Entry(self.frame, 
                        textvariable=DoubleVar()).grid(row=el['row'], 
                        column=el['col'][0], 
                        padx=[10, 20], 
                        pady=[30, 0]), 
            Label(self.frame, 
                    text=el['text'], 
                    justify=LEFT, 
                    wraplength=500).grid(row=el['row'], 
                    column=el['col'][1], 
                    columnspan= 2, 
                    pady=[30, 0])) for el in widgets.list_entries if el['id'] not in (8,9)]
        else:
            self.header = Label(self.frame ,text="Кзф = [0,65 Ч К1 Ч Кст Ч Kпер / (V1 Ч Кст Ч К1 + (1 - Kш) Ч (Ко Ч К ст + 1) Ч Kпер Ч Kм)] Ч KНЗ    (Г.6) ")
            self.header.grid(row=0, column=0, columnspan= 2, ipadx=0, ipady=0, padx=[50, 50], pady=[30, 0])
            [(ttk.Entry(self.frame, 
                        textvariable=DoubleVar()).grid(row=el['row'], 
                        column=el['col'][0], 
                        padx=[10, 20], 
                        pady=[30, 0]), 
            Label(self.frame, 
                    text=el['text'], 
                    justify=LEFT, 
                    wraplength=500).grid(row=el['row'], 
                    column=el['col'][1], 
                    columnspan= 2, 
                    pady=[30, 0])) for el in widgets.list_entries if el['id'] not in (6,7)]


        #определение кнопок

        def btn_closed(self):
            self.destroy()

        def btn_prev(self):
            main()
            self.destroy()

        def solved(self):
            pass

        list_btn = [
            {'id': 0,'text': 'Назад', 'func': lambda: btn_prev(self)},
            {'id': 1,'text': 'Закрити', 'func': lambda: btn_closed(self)},
            {'id': 2, 'text': 'Розрахувати', 'func': lambda: solved(self)}
        ]

        [ttk.Button(self.frame, 
                    text=el['text'], 
                    command=el['func']).grid(row=9, 
                                             column=el['id'], 
                                             pady=[30, 0]) for el in list_btn]