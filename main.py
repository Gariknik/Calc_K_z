from openpyxl import Workbook
from tkinter import *
from tkinter import ttk
import classes.Window as Window

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
        self.window = Window.Window(Main, result)
        self.destroy()


if __name__ == "__main__":
    root = Main()
    root.mainloop()