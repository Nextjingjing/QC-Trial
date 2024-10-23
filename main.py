# main.py

import tkinter as tk
from Frames import InputFrame  # นำเข้า InputFrame จากแพ็กเกจ Frames

def main():
    root = tk.Tk()
    root.title("Input Frame Example")
    
    input_frame = InputFrame(root)
    input_frame.pack(padx=20, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
