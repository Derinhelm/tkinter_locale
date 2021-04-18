import tkinter as tk
import gettext

gettext.install('app', localedir='po')


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.tb = tk.Button(self, text=_("Кнопка"), font = 'Helvetica', width=30)
        self.tb.grid(row=1, column=0)
        self.lab = tk.Label(text=_("Текст"), width=30)
        self.lab.grid(row=2, column=0)


#app = Application()
#app.mainloop()
root = tk.Tk()
root.title(_("Приложение"))
root.geometry("300x50")
app = Application(root)
root.mainloop()
