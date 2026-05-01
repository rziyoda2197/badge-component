import tkinter as tk

class Badge:
    def __init__(self, master, text, color, size):
        self.master = master
        self.text = text
        self.color = color
        self.size = size
        self.badge = tk.Label(master, text=text, bg=color, fg="white", font=("Arial", size))
        self.badge.pack()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.badge1 = Badge(self, "New", "blue", 12)
        self.badge2 = Badge(self, "Updated", "green", 14)
        self.badge3 = Badge(self, "Deleted", "red", 16)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
