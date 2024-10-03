import customtkinter as ctk
from tkinter import PhotoImage, filedialog
import os

class Label(ctk.CTkLabel):
    def __init__(self, ui, index, text, order_pack, editable=True):
        super().__init__(ui)
        self.index = index
        self.ui = ui
        self.app = ui.app
        self.order_pack = order_pack
        self.text = text
        self.editable = editable
        self.configure(text=self.text)
        self.entry = None

        if self.editable:
            self.bind("<Double-Button-1>", self.enable_editing)

    def enable_editing(self, event):
        # Create an entry widget with the same dimensions as the label
        self.entry = ctk.CTkEntry(self.ui, textvariable=ctk.StringVar(value=self.text), width=self.winfo_width(), height=self.winfo_height())
        self.entry.place(x=self.winfo_x(), y=self.winfo_y())
        self.entry.focus()
        self.entry.bind("<Return>", self.save_edit)
        self.entry.bind("<FocusOut>", self.save_edit)

    def save_edit(self, event):
        if self.entry:
            # Save the edited text
            self.text = self.entry.get()
            self.configure(text=self.text)
            self.entry.unbind("<Return>")
            self.entry.unbind("<FocusOut>")
            self.entry.destroy()
            self.entry = None
            self.bind("<Double-Button-1>", self.enable_editing)