from tkinter import *
from tkinter import ttk
import lib.widgets as widgets
from decimal import Decimal, ROUND_HALF_DOWN


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
        self.geometry("900x900")
        self.resizable(False, False)
        self.focus_force()
        self.result = 0

        #выбор набора парамметров исходя из выбранной формули
        self.id = id
        self.frame = Frame(self, padx=0, pady=0)
        self.frame.pack()
        self.list_params = []
        self.entries = []
        if self.id == '1':
            self.header = Label(self.frame, 
                                text="Кзф = [0,77 x К1  x К ст  x Кп / ((1-Кш) x  ((К’о x Кст +1) + Кп x (Ко x К ст +1)) x К м)] x KНЗ,        (Г.7) ",
                                font=("Arial", 12))
            self.header.grid(row=0, column=0, columnspan= 3, ipadx=0, ipady=0, padx=[50, 50], pady=[30, 0])
            for el in widgets.list_entries:
                if el['id'] not in (8,9):
                    entry = Entry(self.frame, 
                        textvariable=DoubleVar(),
                        justify=CENTER)
                    entry.grid(row=el['row'], 
                        column=el['col'][0], 
                        padx=[10, 20], 
                        pady=[20, 0])
                    Label(self.frame, 
                        text=el['text'], 
                        justify=LEFT, 
                        wraplength=500).grid(row=el['row'], 
                        column=el['col'][1], 
                        columnspan= 2, 
                        pady=[30, 0])
                    self.entries.append(entry)
        else:
            self.header = Label(self.frame,
                                text="Кзф = [0,65 x К1 x Кст x Kпер / (V1 x Кст x К1 + (1 - Kш) x (Ко x К ст + 1) x Kпер x Kм)] x KНЗ    (Г.6) ",
                                font=("Arial", 12))
            
            self.header.grid(row=0, column=0, columnspan= 3, ipadx=0, ipady=0, padx=[50, 50], pady=[30, 0])
            for el in widgets.list_entries:
                if el['id'] not in (6,7):
                    entry = Entry(self.frame, 
                        textvariable=DoubleVar(),
                        justify=CENTER)
                    entry.grid(row=el['row'], 
                        column=el['col'][0], 
                        padx=[10, 20], 
                        pady=[20, 0])
                    Label(self.frame, 
                        text=el['text'], 
                        justify=LEFT, 
                        wraplength=550).grid(row=el['row'], 
                        column=el['col'][1], 
                        columnspan= 2, 
                        pady=[30, 0])
                    self.entries.append(entry)

        self.print_result = Label(self.frame ,text="Результат: 0", font=("Arial", 11), fg='#008000')
        self.print_result.grid(row=9, column=0, columnspan= 3, ipadx=0, ipady=0, padx=[50, 50], pady=[30, 0])
        #определение кнопок

        def btn_closed(self):
            self.destroy()

        def btn_prev(self):
            main()
            self.destroy()

        def solved(self):

            for entry in self.entries:
                el = entry.get()
                self.list_params.append(Decimal(el))

            if self.id == '1':
                K1, K_st, K0, Km, Ksh, Knz, Kp, K10 = self.list_params
                numerator = Decimal(0.77) * K1  * K_st  * Kp
                denominator = (1 - Ksh) * ((K10 * K_st +1) + Kp * (K0 * K_st + 1)) * Km
                numerator.quantize(Decimal("1.000"), ROUND_HALF_DOWN)
                denominator.quantize(Decimal("1.000"), ROUND_HALF_DOWN)
                self.result = (numerator / denominator) * Knz
                
            else:
                K1, K_st, K0, Km, Ksh, Knz, Kper, V1 = self.list_params
                numerator = Decimal(0.65) * K1 * K_st * Kper
                denominator = V1 * K_st * K1 + (1 - Ksh) * (K0 * K_st + 1) * Kper * Km
                numerator.quantize(Decimal("1.000"), ROUND_HALF_DOWN)
                denominator.quantize(Decimal("1.000"), ROUND_HALF_DOWN)
                self.result = (numerator / denominator) * Knz
            
            self.print_result['text'] = 'Результат: Kзф =' + str(self.result.quantize(Decimal("1.00"), ROUND_HALF_DOWN))


            

        list_btn = [
            {'id': 0,'text': 'Назад', 'func': lambda: btn_prev(self)},
            {'id': 1,'text': 'Закрити', 'func': lambda: btn_closed(self)},
            {'id': 2, 'text': 'Розрахувати', 'func': lambda: solved(self)}
        ]

        [ttk.Button(self.frame, 
                    text=el['text'], 
                    command=el['func']).grid(row=10, 
                                             column=el['id'], 
                                             pady=[30, 0]) for el in list_btn]