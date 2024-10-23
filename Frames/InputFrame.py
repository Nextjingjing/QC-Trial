# Frames/InputFrame.py

import tkinter as tk
from tkinter import ttk, messagebox

class InputFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Attributes to store the input values
        self.n = None
        self.p = None
        self.c = None
        
        # Create and place Label and Entry for n
        self.label_n = ttk.Label(self, text="n: Sample Size")
        self.label_n.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        
        self.entry_n = ttk.Entry(self)
        self.entry_n.grid(row=0, column=1, padx=10, pady=5)
        
        # Create and place Label and Entry for p
        self.label_p = ttk.Label(self, text="p: Probability of Defect")
        self.label_p.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        
        self.entry_p = ttk.Entry(self)
        self.entry_p.grid(row=1, column=1, padx=10, pady=5)
        
        # Create and place Label and Entry for c
        self.label_c = ttk.Label(self, text="c: Acceptance Number")
        self.label_c.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        
        self.entry_c = ttk.Entry(self)
        self.entry_c.grid(row=2, column=1, padx=10, pady=5)
        
        # Button to retrieve and store the input values
        self.button_submit = ttk.Button(self, text="Submit", command=self.get_inputs)
        self.button_submit.grid(row=3, column=0, columnspan=2, pady=10)
        
    def get_inputs(self):
        try:
            self.n = int(self.entry_n.get())
            self.p = float(self.entry_p.get())
            self.c = int(self.entry_c.get())
            print(f"n: {self.n}, p: {self.p}, c: {self.c}")
            # You can add additional code here after retrieving the values
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for n, p, and c.")
