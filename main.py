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
        #Вставка формул в главном окне и добавление переключателей RadioBtn
        self.position = {"padx": 50, "pady": [50,25], "anchor": CENTER}

        self.list_formulas = [
                                {"id": 1, "text": """Розрахунковий коефіцієнт послаблення радіаційного  впливу  Кзф для вбудованих ПРУ чи 
                                СПП,  які  розташовані  на  відмітках,  що  відповідають  цокольним,  підвальним  та  підземним 
                                поверхам""", "img": PhotoImage(file="./images/formula_1.png")},
                                {"id": 2, "text": """Розрахунковий коефіцієнт послаблення радіаційного  впливу  Кзф для вбудованих ПРУ чи
                                СПП з відміткою підлоги, що заглиблена менше ніж на 1,7 м відносно 
                                планувальної відмітки землі""", "img": PhotoImage(file="./images/formula_2.png")}            
                            ]

        self.work_formula=StringVar(value=self.list_formulas[0]['id']) #по умолчанию выбран элемент formula_1

        self.header = ttk.Label(textvariable=self.list_formulas[0]['text'])
        self.header.pack(**self.position)

        for f in self.list_formulas:
            self.r_btn = Radiobutton(value=f["text"], text=f["text"], variable=self.work_formula, image=f["img"], compound="bottom")
            self.r_btn.pack(**self.position)

        #Кнопка для направления к соответствующему расчёту
        self.link_btn = ttk.Button(text="Пейти до розрахунку", width=30, command=self.click_for_solve)
        self.link_btn.pack()
    def click_for_solve(self):
        self.window = Window()


#Диалоговые окна
class Window(Tk):
    """
    класс окна расчета по одной из двух формул
    """
    def __init__(self):
        super().__init__()

        #конфигурация окна
        self.title("Розрахунок")
        self.geometry("800x600")

        #определение кнопок
        self.close_button = ttk.Button(self, text="Закрити")
        self.close_button["command"] = self.btn_closed
        self.close_button.grid(row=0, column=1, ipadx=10, ipady=5, padx=150, pady=[500,50], sticky=NSEW)

        self.solve_button = ttk.Button(self, text="Розрахувати")
        self.solve_button["command"] = self.solved
        self.solve_button.grid(row=0, column=2, ipadx=10, ipady=5, padx=150, pady=[500,50], sticky=NSEW)

    def btn_closed(self):
        self.destroy()

    def solved(self):
        pass


if __name__ == "__main__":
    root = Main()
    root.mainloop()