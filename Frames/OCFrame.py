# Frames/OCFrame.py

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import comb

class OCFrame(tk.Frame):
    def __init__(self, parent, input_frame):
        super().__init__(parent)
        self.input_frame = input_frame  # รับ InputFrame เพื่อเข้าถึง n, p, c

        # ปุ่มสำหรับคำนวณและแสดงกราฟ OC
        self.button_show_oc = ttk.Button(self, text="Show OC Curve", command=self.show_oc_curve)
        self.button_show_oc.grid(row=0, column=0, padx=10, pady=10)

        # กรอบสำหรับแสดงกราฟ
        self.plot_frame = ttk.Frame(self)
        self.plot_frame.grid(row=1, column=0, padx=10, pady=10)

    def calculate_pa(self, n, p, c):
        pa = 0
        for k in range(0, c + 1):
            pa += comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        return pa

    def show_oc_curve(self):
        try:
            n = self.input_frame.n
            c = self.input_frame.c

            if n is None or c is None:
                raise ValueError("กรุณากรอกข้อมูลใน InputFrame ก่อนแสดงกราฟ OC")

            # สร้างช่วงของ p จาก 0 ถึง 1
            p_values = [i / 1000 for i in range(0, 1001)]
            pa_values = [self.calculate_pa(n, p, c) for p in p_values]

            # ล้างกราฟก่อนหน้า
            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            # สร้าง Figure และ Plot
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(p_values, pa_values, label='OC Curve')
            ax.set_title('Operating Characteristic (OC) Curve')
            ax.set_xlabel('p: Fraction Defective')
            ax.set_ylabel('Pa: Probability of Acceptance')
            ax.grid(True)
            ax.legend()

            # แปลงกราฟเป็น Tkinter Widget
            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

        except Exception as e:
            tk.messagebox.showerror("Error", str(e))
