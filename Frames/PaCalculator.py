# Frames/PaCalculator.py

import tkinter as tk
from tkinter import ttk
from math import comb  # ใช้สำหรับคำนวณทวีนิยมแบบ binomial

class PaCalculator(tk.Frame):
    def __init__(self, parent, input_frame):
        super().__init__(parent)
        self.input_frame = input_frame  # รับ InputFrame เพื่อเข้าถึง n, p, c

        # ปุ่มสำหรับคำนวณ Pa
        self.button_calculate = ttk.Button(self, text="Calculate Pa", command=self.calculate_pa)
        self.button_calculate.grid(row=0, column=0, padx=10, pady=10)

        # Label สำหรับแสดงผลลัพธ์ Pa
        self.label_pa = ttk.Label(self, text="Pa: ")
        self.label_pa.grid(row=0, column=1, padx=10, pady=10, sticky='w')

    def calculate_pa(self):
        try:
            n = self.input_frame.n
            p = self.input_frame.p
            c = self.input_frame.c

            if n is None or p is None or c is None:
                raise ValueError("กรุณากรอกข้อมูลใน InputFrame ก่อนคำนวณ Pa")

            # คำนวณ Pa โดยใช้การแจกแจงแบบ binomial
            pa = 0
            for k in range(0, c + 1):
                pa += comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

            self.label_pa.config(text=f"Pa: {pa:.4f}")
        except Exception as e:
            self.label_pa.config(text=f"Error: {e}")
