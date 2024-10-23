# main.py

import tkinter as tk
from tkinter import messagebox
from Frames import InputFrame, PaCalculator, OCFrame

def main():
    root = tk.Tk()
    root.title("Probability of Accepting the Lot (Pa) and OC Curve")

    # สร้าง InputFrame และวางไว้ทางบน
    input_frame = InputFrame(root)
    input_frame.pack(padx=20, pady=10)

    # สร้าง PaCalculator โดยส่ง input_frame ไปให้
    pa_calculator = PaCalculator(root, input_frame)
    pa_calculator.pack(padx=20, pady=10)

    # สร้าง OCFrame โดยส่ง input_frame ไปให้
    oc_frame = OCFrame(root, input_frame)
    oc_frame.pack(padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
