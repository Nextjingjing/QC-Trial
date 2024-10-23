# main.py

import tkinter as tk
from tkinter import ttk
from Frames import InputFrame, PaCalculator, OCFrame

def main():
    root = tk.Tk()
    root.title("Probability of Accepting the Lot (Pa) and OC Curve")

    # Configure the main window's grid
    root.columnconfigure(0, weight=1)  # Left column
    root.columnconfigure(1, weight=3)  # Right column
    root.rowconfigure(0, weight=1)

    # Create left and right frames
    left_frame = ttk.Frame(root, padding=(10, 10))
    left_frame.grid(row=0, column=0, sticky='nsew')

    right_frame = ttk.Frame(root, padding=(10, 10))
    right_frame.grid(row=0, column=1, sticky='nsew')

    # Configure grid weights for left and right frames
    left_frame.columnconfigure(0, weight=1)
    left_frame.rowconfigure(0, weight=0)
    left_frame.rowconfigure(1, weight=0)

    right_frame.columnconfigure(0, weight=1)
    right_frame.rowconfigure(0, weight=1)

    # Create and place InputFrame in left_frame
    input_frame = InputFrame(left_frame)
    input_frame.grid(row=0, column=0, sticky='nw')

    # Create and place PaCalculator in left_frame
    pa_calculator = PaCalculator(left_frame, input_frame)
    pa_calculator.grid(row=1, column=0, pady=20, sticky='nw')

    # Create and place OCFrame in right_frame
    oc_frame = OCFrame(right_frame, input_frame)
    oc_frame.grid(row=0, column=0, sticky='nsew')

    # Set a minimum size for the window
    root.geometry("1200x700")

    root.mainloop()

if __name__ == "__main__":
    main()
