# Frames/OCFrame.py

import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import comb

class OCFrame(tk.Frame):
    def __init__(self, parent, input_frame):
        super().__init__(parent)
        self.input_frame = input_frame  # Receive InputFrame to access n, p, c

        # Button to calculate and display the OC Curve
        self.button_show_oc = ttk.Button(self, text="Show OC Curve", command=self.show_oc_curve)
        self.button_show_oc.pack(padx=10, pady=10)

        # Frame to hold the plot
        self.plot_frame = ttk.Frame(self)
        self.plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

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
                raise ValueError("Please enter the required data in the InputFrame before displaying the OC Curve.")

            # Create a range of p values from 0 to 1 with higher resolution
            p_values = [i / 10000 for i in range(0, 10001)]
            pa_values = [self.calculate_pa(n, p, c) for p in p_values]

            # Clear previous plots
            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            # Create Figure and Plot with enhanced scaling
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(p_values, pa_values, label='OC Curve', color='blue')
            ax.set_title('Operating Characteristic (OC) Curve', fontsize=14)
            ax.set_xlabel('p: Fraction Defective', fontsize=12)
            ax.set_ylabel('Pa: Probability of Acceptance', fontsize=12)
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            ax.legend(fontsize=12)
            ax.tick_params(axis='both', which='major', labelsize=10)

            # Improve layout
            fig.tight_layout()

            # Embed the plot in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", str(e))
