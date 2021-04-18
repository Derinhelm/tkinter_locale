import tkinter as tk
import gettext

gettext.install('app', localedir='po')


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.tb = tk.Button(self, text=_("Кнопка"), font = 'Helvetica')
        self.tb.grid(row=1, column=0)
        self.lab = tk.Label(text=_("Текст"))
        self.lab.grid(row=2, column=0)
        self.lab2 = tk.Label(text=_("Чуть-чуть текста"))
        self.lab2.grid(row=2, column=1)



app = Application()
app.mainloop()
