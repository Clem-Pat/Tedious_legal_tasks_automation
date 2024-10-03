import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
import tkinter as tk
from interface.button import Button
from interface.canvas import Canvas
from interface.label import Label

class UI(ctk.CTk):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Image Drop on Canvas")
        self.geometry("800x600")

        self.buttons = [Button(self, i) for i in range(2)]
        self.canvas  = [Canvas(self, i) for i in range(1)]
        self.labels  = [Label(self, i, "Identity", -1) for i in range(1)]
        self.pack_elements()

    def pack_elements(self):
        objects = self.labels + self.buttons + self.canvas
        sorted_objects = sorted(objects, key=lambda obj: obj.order_pack)
        
        for element in sorted_objects:
            if isinstance(element, Label):
                element.pack()
            else:
                element.pack(pady = 10)

    def get_object(self, name):
        objects = self.buttons + self.canvas + self.labels
        for obj in objects:
            if obj.name == name:
                return obj
        return None
    
    def add_info(self, key, value, editable=True):
        self.labels.append(Label(self, -1, f"{key}: {value}", 2, editable))
        self.pack_elements()