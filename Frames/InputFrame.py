# Frames/InputFrame.py

import tkinter as tk
from tkinter import ttk

class InputFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # สร้างและวาง Label และ Entry สำหรับ n
        self.label_n = ttk.Label(self, text="n: ขนาดของ Sampling")
        self.label_n.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        
        self.entry_n = ttk.Entry(self)
        self.entry_n.grid(row=0, column=1, padx=10, pady=5)
        
        # สร้างและวาง Label และ Entry สำหรับ p
        self.label_p = ttk.Label(self, text="p: ความน่าจะเป็นที่จะเจอของเสีย")
        self.label_p.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        
        self.entry_p = ttk.Entry(self)
        self.entry_p.grid(row=1, column=1, padx=10, pady=5)
        
        # สร้างและวาง Label และ Entry สำหรับ c
        self.label_c = ttk.Label(self, text="c: ปริมาณของเสียที่ยังยอมรับได้")
        self.label_c.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        
        self.entry_c = ttk.Entry(self)
        self.entry_c.grid(row=2, column=1, padx=10, pady=5)
        
        # ปุ่มเพื่อดึงค่าที่กรอกและเก็บไว้ในแอตทริบิวต์
        self.button_submit = ttk.Button(self, text="Submit", command=self.get_inputs)
        self.button_submit.grid(row=3, column=0, columnspan=2, pady=10)
        
        # แอตทริบิวต์สำหรับเก็บค่าที่กรอก
        self.n = None
        self.p = None
        self.c = None

    def get_inputs(self):
        try:
            self.n = int(self.entry_n.get())
            self.p = float(self.entry_p.get())
            self.c = int(self.entry_c.get())
            print(f"n: {self.n}, p: {self.p}, c: {self.c}")
            # คุณสามารถเพิ่มโค้ดเพิ่มเติมที่ต้องการหลังจากรับค่าได้ที่นี่
        except ValueError:
            tk.messagebox.showerror("Input Error", "กรุณากรอกข้อมูลที่ถูกต้องสำหรับ n, p, และ c")
