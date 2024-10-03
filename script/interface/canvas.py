import customtkinter as ctk
from tkinter import PhotoImage, filedialog
import os

class Canvas(ctk.CTkCanvas):
    def __init__(self, ui, index):
        super().__init__(ui)
        self.index = index
        self.ui = ui
        self.app = ui.app
        self.order_pack = -1
        self.name = ""
        self.height, self.width = 200, 500

        if index == 0:
            self.name = "image_render"
            self.configure(bg="white", height=self.height, width=self.width)
            self.order_pack = 0
            #self.canvas.bind("<Button-1>", self.on_click)
