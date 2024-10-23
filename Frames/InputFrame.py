# Frames/InputFrame.py

import tkinter as tk
from tkinter import ttk, messagebox

class InputFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#FFF9C4')  # สีพื้นหลังสีเหลืองอ่อน

        # Initialize Style
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 12), background='#FFF9C4')
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12, 'bold'))
        self.style.configure('Status.TLabel', font=('Helvetica', 10), foreground='red', background='#FFF9C4')
        self.style.configure('Success.TLabel', font=('Helvetica', 10), foreground='green', background='#FFF9C4')

        # Create a LabelFrame to group input fields
        self.input_group = tk.LabelFrame(self, text="Input Parameters", font=('Helvetica', 12, 'bold'), bg='#FFF9C4', padx=20, pady=10)
        self.input_group.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        # Configure grid within LabelFrame
        self.input_group.columnconfigure(1, weight=1)

        # Create and place Label and Entry for n
        self.label_n = ttk.Label(self.input_group, text="n: Sample Size", background='#FFF9C4')
        self.label_n.grid(row=0, column=0, padx=10, pady=10, sticky='e')

        self.entry_n = ttk.Entry(self.input_group, width=25)
        self.entry_n.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        # self.entry_n.insert(0, "Enter an integer (e.g., 100)")  # ลบคำใบ้ออก

        # Create and place Label and Entry for p
        self.label_p = ttk.Label(self.input_group, text="p: Probability of Defect", background='#FFF9C4')
        self.label_p.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.entry_p = ttk.Entry(self.input_group, width=25)
        self.entry_p.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        # self.entry_p.insert(0, "Enter a float between 0 and 1 (e.g., 0.05)")  # ลบคำใบ้ออก

        # Create and place Label and Entry for c
        self.label_c = ttk.Label(self.input_group, text="c: Acceptance Number", background='#FFF9C4')
        self.label_c.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.entry_c = ttk.Entry(self.input_group, width=25)
        self.entry_c.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        # self.entry_c.insert(0, "Enter a non-negative integer (e.g., 5)")  # ลบคำใบ้ออก

        # Create and place Submit Button
        self.button_submit = ttk.Button(self.input_group, text="Submit", command=self.get_inputs)
        self.button_submit.grid(row=3, column=0, columnspan=2, pady=20)

        # Create Status Frame for displaying messages
        self.status_frame = ttk.Frame(self, style='Status.TLabel')
        self.status_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='ew')

        self.status_label = ttk.Label(self.status_frame, text="", style='Status.TLabel')
        self.status_label.pack(anchor='w')

        # Create Labels to display current values of n, p, c (ซ่อนเริ่มต้น)
        self.current_values_frame = ttk.Frame(self)
        self.current_values_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky='ew')

        self.label_current_n = ttk.Label(self.current_values_frame, text="", style='TLabel')
        self.label_current_p = ttk.Label(self.current_values_frame, text="", style='TLabel')
        self.label_current_c = ttk.Label(self.current_values_frame, text="", style='TLabel')

        # ซ่อน labels ตอนเริ่มต้น
        self.label_current_n.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.label_current_p.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.label_current_c.grid(row=0, column=2, padx=10, pady=5, sticky='w')

        self.label_current_n.grid_remove()
        self.label_current_p.grid_remove()
        self.label_current_c.grid_remove()

    def get_inputs(self):
        """
        Retrieve and validate input values for n, p, and c.
        """
        try:
            # Retrieve and convert inputs
            n_input = self.entry_n.get().strip()
            p_input = self.entry_p.get().strip()
            c_input = self.entry_c.get().strip()

            # Validate and convert n
            if not n_input:
                raise ValueError("Sample size (n) cannot be empty.")
            self.n = int(n_input)
            if self.n <= 0:
                raise ValueError("Sample size (n) must be a positive integer.")

            # Validate and convert p
            if not p_input:
                raise ValueError("Probability of defect (p) cannot be empty.")
            self.p = float(p_input)
            if not (0 <= self.p <= 1):
                raise ValueError("Probability of defect (p) must be between 0 and 1.")

            # Validate and convert c
            if not c_input:
                raise ValueError("Acceptance number (c) cannot be empty.")
            self.c = int(c_input)
            if self.c < 0:
                raise ValueError("Acceptance number (c) must be a non-negative integer.")

            # Update status to success
            self.update_status(f"Inputs submitted successfully: n={self.n}, p={self.p}, c={self.c}", success=True)

            # แสดงค่าที่ใช้อยู่
            self.label_current_n.config(text=f"n: {self.n}")
            self.label_current_p.config(text=f"p: {self.p}")
            self.label_current_c.config(text=f"c: {self.c}")

            # แสดง labels
            self.label_current_n.grid()
            self.label_current_p.grid()
            self.label_current_c.grid()

            # Print the inputs to the console (for debugging)
            print(f"n: {self.n}, p: {self.p}, c: {self.c}")

            # คุณสามารถเพิ่มโค้ดเพิ่มเติมที่นี่เพื่อเรียกใช้ฟังก์ชันอื่นหลังการส่งข้อมูล

        except ValueError as ve:
            # Display error message in status label
            self.update_status(str(ve), success=False)
        except Exception as e:
            # Handle unexpected errors
            self.update_status(f"An unexpected error occurred: {str(e)}", success=False)

    def update_status(self, message, success=True):
        """
        Update the status label with a message.
        :param message: The message to display.
        :param success: Boolean indicating if the message is a success or error.
        """
        if success:
            self.status_label.config(text=message, foreground='green')
        else:
            self.status_label.config(text=message, foreground='red')
