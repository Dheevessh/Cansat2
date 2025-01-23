import tkinter as tk
from tkinter import ttk

class MapView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Map View")
        self.window.geometry("600x400")

        ttk.Label(self.window, text="Map displaying GPS data will be here.").pack(pady=20)

    def show(self):
        self.window.mainloop()
