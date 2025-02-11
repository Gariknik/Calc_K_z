from openpyxl import Workbook
from tkinter import *
from tkinter import ttk

#Главное окно
class Main(Tk):
    """
    класс главного окна приложения
    """
    def __init__(self):
        super().__init__()    

        self.title("Розрахунок коефіцієнта захисту Кз для ПРУ") #устанавливаем заголовок окна
        self.geometry("800x600")
        self.resizable(False, False)
        #Вставка формул в главном окне и добавление переключателей RadioBtn
        self.position = {"padx": 50, "pady": [50,25], "anchor": CENTER}

        self.list_formulas = [
                                {"id": 1, "text": """Розрахунковий коефіцієнт послаблення радіаційного  впливу  Кзф для вбудованих ПРУ чи 
                                СПП,  які  розташовані  на  відмітках,  що  відповідають  цокольним,  
                                підвальним  та  підземним поверхам""", "img": PhotoImage(file="./images/formula_1.png")},
                                {"id": 2, "text": """Розрахунковий коефіцієнт послаблення радіаційного  впливу  Кзф для вбудованих ПРУ чи
                                СПП з відміткою підлоги, що заглиблена менше ніж на 1,7 м відносно 
                                планувальної відмітки землі""", "img": PhotoImage(file="./images/formula_2.png")}            
                            ]

        self.work_formula=StringVar(value=self.list_formulas[0]['id']) #по умолчанию выбран элемент formula_1

        self.header = ttk.Label(textvariable=self.list_formulas[0]['text'])
        self.header.pack(**self.position)

        radios = [Radiobutton(value=f["id"], text=f["text"], variable=self.work_formula, image=f["img"], compound="bottom") for f in self.list_formulas]

        for radio in radios:
            radio.pack(**self.position)

        #Кнопка для направления к соответствующему расчёту
        self.link_btn = ttk.Button(text="Пейти до розрахунку", width=30, command=self.click_for_solve)
        self.link_btn.bind("<Deactivate>", self.click_for_solve)
        self.link_btn.pack()
    def click_for_solve(self):
        result = self.work_formula.get()
        self.window = Window(result)
        self.destroy()



#Диалоговые окна
class Window(Tk):
    """
    класс окна расчета по одной из двух формул
    """
    def __init__(self, id):
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

        self.K_1 = ttk.Entry(self.frame, textvariable=DoubleVar())
        self.K_1.grid(row=1, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
        self.label_K_1 = Label(self.frame, text='K1 -  коефіцієнт,  що  враховує  частку  радіації,  яка  проникає  крізь  стіни  ПРУ  чи  СПП  та розраховується за формулою Г.8, з урахуванням положень п. Г.2.5', 
                                    justify=LEFT, 
                                    wraplength=500)
        self.label_K_1.grid(row=1, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])


        self.K_st = ttk.Entry(self.frame, textvariable=DoubleVar())
        self.K_st.grid(row=2, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
        self.label_K_st = Label(self.frame, text='Kст - кратність послаблення стінами ПРУ чи СПП первинного випромінювання в залежності від ваги огороджувальної конструкції по вертикалі, Н/м.кв. (кг/м.кв.) (в тому числі багатошарової), яка визначається за таблицею Г.5, з урахуванням положень п. Г.2.6', 
                                    justify=LEFT, 
                                    wraplength=500)
        self.label_K_st.grid(row=2, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])


        self.K_0 = ttk.Entry(self.frame, textvariable=DoubleVar())
        self.K_0.grid(row=3, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
        self.label_K_0 = Label(self.frame, text='K0 -  коефіцієнт, який враховує безпосереднє проникнення в ПРУ чи СПП випромінювання, крізь  отвори  в  огороджувальних  конструкціях,  і  визначається  згідно  формул  Г.13  –  Г.15,  з урахуванням положень п. Г.2.8', 
                                    justify=LEFT, 
                                    wraplength=500)
        self.label_K_0.grid(row=3, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])

        self.K_m = ttk.Entry(self.frame, textvariable=DoubleVar())
        self.K_m.grid(row=4, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
        self.label_K_m = Label(self.frame, text='Kм -  коефіцієнт, що враховує  зниження  дози  радіації  в ПРУ чи СПП,  розташованих  у  районі забудови, від екрануючої дії сусідніх споруд, який приймається за таблицею Г.7 ', 
                                justify=LEFT, 
                                wraplength=500)
        self.label_K_m.grid(row=4, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])

        self.K_sh = ttk.Entry(self.frame, textvariable=DoubleVar())
        self.K_sh.grid(row=5, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
        self.label_K_sh = Label(self.frame, text='Kш -   коефіцієнт, який залежить від ширини ПРУ чи СПП та приймається за таблицею Г.6', 
                                    justify=LEFT, 
                                    wraplength=500)
        self.label_K_sh.grid(row=5, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])

        self.K_nz = ttk.Entry(self.frame, textvariable=DoubleVar())
        self.K_nz.grid(row=6, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
        self.label_K_nz = Label(self.frame, text='''Kнз -   коефіцієнт, що  враховує невідворотність зараження радіоактивними опадами конструкцій покриття ПРУ чи СПП, приймається: 
-  для наземних ПРУ чи СПП, які розміщені окремо, вбудовані в одноповерхові будівлі чи прибудовані до будь-яких будівель: 0,45; 
-  для вбудованих ПРУ чи СПП у багатоповерхові будівлі, а також розміщених на відмітках цокольного, підвального та підземного поверху будівлі зі штучних кам’яних матеріалів та залізобетонним перекриттям над 1-м поверхом: 0,8; 
-  для  вбудованих  ПРУ  чи  СПП,  які  розміщені  на  відмітці  підземного  поверху,  якщо покриття ПРУ чи СПП не являється конструкцією, яка в тому числі утворює підлогу 1-го поверху (між ПРУ чи СПП та підлогою 1-го поверху, знаходиться додатковий поверх, в тому числі технічний): 1. ''', 
                                justify=LEFT, 
                                wraplength=500)
        self.label_K_nz.grid(row=6, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])


        if self.id == '1':
            self.header = Label(self.frame, text="Кзф = [0,77 Ч К1  Ч К ст  Ч Кп / ((1-Кш) Ч  ((К’о Ч Кст +1) + Кп Ч (Ко Ч К ст +1)) Ч К м)] Ч KНЗ,        (Г.7) ")
            self.header.grid(row=0, column=0, columnspan= 2, ipadx=0, ipady=0, padx=[50, 50], pady=[30, 0])

            self.K_p = ttk.Entry(self.frame, textvariable=DoubleVar())
            self.K_p.grid(row=7, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
            self.label_K_p = Label(self.frame, text='Kп -   кратність послаблення покриттям ПРУ чи СПП вторинного випромінювання, розсіяного у  приміщенні  поверху,  над  укриттям,  що  визначається  залежно  від  ваги  огороджувальної конструкції, Н/м.кв. (кг/м.кв.) (в тому числі багатошарової), яка визначається за таблицею Г.5, з урахуванням положень п. Г.2.7', 
                                    justify=LEFT, 
                                    wraplength=500)
            self.label_K_p.grid(row=7, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])
              
            self.K_01 = ttk.Entry(self.frame, textvariable=DoubleVar())
            self.K_01.grid(row=8, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
            self.label_K_01 = Label(self.frame, text="K'0 - коефіцієнт  отворів  у  стінах  поверху  будівлі,  нижче  планувальної  відмітки  якого вбудовано ПРУ чи СПП, приймається рівним: 1", 
                                        justify=LEFT, 
                                        wraplength=500)
            self.label_K_01.grid(row=8, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])

        else:
            self.header = Label(self.frame ,text="Кзф = [0,65 Ч К1 Ч Кст Ч Kпер / (V1 Ч Кст Ч К1 + (1 - Kш) Ч (Ко Ч К ст + 1) Ч Kпер Ч Kм)] Ч KНЗ    (Г.6) ")
            self.header.grid(row=0, column=0, columnspan= 2, ipadx=0, ipady=0, padx=[50, 50], pady=[30, 0])

            self.K_per = ttk.Entry(self.frame, textvariable=DoubleVar())
            self.K_per.grid(row=7, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
            self.label_K_per = Label(self.frame, text="Kпер -   кратність  послаблення  первинного  випромінювання  покриттям  ПРУ  чи  СПП,  в залежності від ваги огороджувальної конструкції, Н/м.кв. (кг/м.кв.) (в тому числі багатошарової), яка визначається за таблицею Г.5, з урахуванням положень п. Г.2.7", 
                                        justify=LEFT, 
                                        wraplength=500)
            self.label_K_per.grid(row=7, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])

            self.V_1 = ttk.Entry(self.frame, textvariable=DoubleVar())
            self.V_1.grid(row=8, column=0, ipadx=0, ipady=0, padx=[10, 20], pady=[30, 0])
            self.label_V_1 = Label(self.frame, text="V1 -    коефіцієнт,  який  залежить  від  висоти  та  ширини  ПРУ  чи  СПП  та  приймається  за таблицею Г.6, з урахуванням примітки", 
                                    justify=LEFT, 
                                    wraplength=500)
            self.label_V_1.grid(row=8, column=1, columnspan= 2, ipadx=0, ipady=0, padx=[0, 0], pady=[30, 0])
            


        #определение кнопок
        self.prev_button = ttk.Button(self.frame, text="Назад")
        self.prev_button["command"] = self.btn_prev
        self.prev_button.grid(row=9, column=0, ipadx=0, ipady=0, padx=0, pady=[30, 0])

        self.close_button = ttk.Button(self.frame, text="Закрити")
        self.close_button["command"] = self.btn_closed
        self.close_button.grid(row=9, column=1, ipadx=0, ipady=0, padx=0, pady=[30, 0])

        self.solve_button = ttk.Button(self.frame, text="Розрахувати")
        self.solve_button["command"] = self.solved
        self.solve_button.grid(row=9, column=2, ipadx=0, ipady=0, padx=[0,0], pady=[30, 0])

    def btn_closed(self):
        self.destroy()

    def btn_prev(self):
        Main()
        self.destroy()

    def solved(self):
        pass


if __name__ == "__main__":
    root = Main()
    root.mainloop()