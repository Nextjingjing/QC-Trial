# Frames/PaCalculator.py

import tkinter as tk
from tkinter import ttk
from math import comb  # ใช้สำหรับคำนวณทวีนิยมแบบ binomial

class PaCalculator(tk.Frame):
    def __init__(self, parent, input_frame):
        super().__init__(parent, bg='#FFF9C4')  # สีพื้นหลังสีเหลืองอ่อน
        self.input_frame = input_frame  # รับ InputFrame เพื่อเข้าถึง n, p, c

        # Initialize Style
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 12), background='#FFF9C4')
        self.style.configure('TButton', font=('Helvetica', 12, 'bold'))
        self.style.configure('PaLabel.TLabel', font=('Helvetica', 14, 'bold'), foreground='blue', background='#FFF9C4')
        self.style.configure('CurrentVal.TLabel', font=('Helvetica', 12), foreground='black', background='#FFF9C4')

        # Create a LabelFrame to group calculator widgets
        self.calc_group = tk.LabelFrame(self, text="Pa Calculator", font=('Helvetica', 12, 'bold'), bg='#FFF9C4', padx=20, pady=20)
        self.calc_group.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        # Configure grid within LabelFrame
        self.calc_group.columnconfigure(0, weight=1)
        self.calc_group.columnconfigure(1, weight=1)
        self.calc_group.columnconfigure(2, weight=1)

        # Create and place Calculate Pa Button
        self.button_calculate = ttk.Button(self.calc_group, text="Calculate Pa", command=self.calculate_pa)
        self.button_calculate.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # Create and place Pa Result Label
        self.label_pa = ttk.Label(self.calc_group, text="Pa: ", style='PaLabel.TLabel')
        self.label_pa.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Create Frame for displaying current values of n, p, c
        self.current_values_frame = ttk.Frame(self.calc_group, style='CurrentVal.TLabel')
        self.current_values_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

        # Labels to display current values (ซ่อนเริ่มต้น)
        self.label_current_n = ttk.Label(self.current_values_frame, text="", style='CurrentVal.TLabel')
        self.label_current_p = ttk.Label(self.current_values_frame, text="", style='CurrentVal.TLabel')
        self.label_current_c = ttk.Label(self.current_values_frame, text="", style='CurrentVal.TLabel')

        self.label_current_n.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        self.label_current_p.grid(row=0, column=1, padx=5, pady=2, sticky='w')
        self.label_current_c.grid(row=0, column=2, padx=5, pady=2, sticky='w')

        # ซ่อน labels ตอนเริ่มต้น
        self.label_current_n.grid_remove()
        self.label_current_p.grid_remove()
        self.label_current_c.grid_remove()

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

            # แสดงผลลัพธ์ Pa
            self.label_pa.config(text=f"Pa: {pa:.4f}")

            # แสดงค่าที่ใช้อยู่ใน Labels
            self.label_current_n.config(text=f"n: {n}")
            self.label_current_p.config(text=f"p: {p}")
            self.label_current_c.config(text=f"c: {c}")

            # แสดง labels
            self.label_current_n.grid()
            self.label_current_p.grid()
            self.label_current_c.grid()

        except Exception as e:
            self.label_pa.config(text=f"Error: {e}")
            # หากเกิดข้อผิดพลาด ไม่แสดงค่าปัจจุบัน
            self.label_current_n.config(text="")
            self.label_current_p.config(text="")
            self.label_current_c.config(text="")

            self.label_current_n.grid_remove()
            self.label_current_p.grid_remove()
            self.label_current_c.grid_remove()
