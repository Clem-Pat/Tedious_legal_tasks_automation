import customtkinter as ctk
from tkinter import filedialog 
from PIL import Image, ImageTk
import tkinter as tk
import os
import numpy as np
from logic.identity import IdentityExtractor

class Button(ctk.CTkButton):
    def __init__(self, ui, index):
        super().__init__(ui)
        self.index = index
        self.ui = ui
        self.app = ui.app
        self.order_pack = -1
        self.name = ""

        if index == 0:
            self.name = "load_image_button"
            self.configure(text="Load Image", command=self.load_image)
            self.order_pack = 1
            
        elif index == 1:
            self.name = "terminate"
            self.configure(text="Next")
            self.order_pack = 1000


    def load_image(self):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(initialdir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/resources", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            canvas = self.ui.get_object("image_render")
            # Load and display the image
            self.image = Image.open(file_path)
            max_width, max_height = canvas.width, canvas.height
            img_ratio = self.image.width / self.image.height
            target_ratio = max_width / max_height

            # Calculate scaling factors for width and height
            scale_width = max_width / self.image.width
            scale_height = max_height / self.image.height

            # Use the smaller scaling factor to ensure the image fits within the canvas
            scale_factor = min(scale_width, scale_height)

            # Apply the scaling factor
            new_width = int(self.image.width * scale_factor)
            new_height = int(self.image.height * scale_factor)

            # Resize the image
            self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

            self.tk_image = ImageTk.PhotoImage(self.image)
            canvas.delete("all")  # Clear the canvas
            self.image_id = canvas.create_image(0, 0, image=self.tk_image, anchor=tk.NW)
            canvas.config(scrollregion=canvas.bbox(tk.ALL))  # Update the scroll region

            self.app.present_identity(IdentityExtractor(file_path))