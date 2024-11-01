import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from math import comb

class OCFrame(tk.Frame):
    def __init__(self, parent, input_frame):
        super().__init__(parent)  # ลบสีพื้นหลังออก
        self.input_frame = input_frame  # รับ InputFrame เพื่อเข้าถึง n, p, c

        # ลบการกำหนด Style ทั้งหมด

        # Initialize plot variables
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Initialize current limits
        self.initial_xlim = (0, 1)
        self.initial_ylim = (0, 1)  # Assuming Pa ranges from 0 to 1
        self.current_xlim = self.initial_xlim
        self.current_ylim = self.initial_ylim

        # Configure grid layout for OCFrame
        self.columnconfigure(0, weight=0)  # Control Buttons Column
        self.columnconfigure(1, weight=1)  # Plot Column
        self.rowconfigure(0, weight=1)

        # Create Control Frame (Buttons)
        self.control_frame = ttk.Frame(self)
        self.control_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # Add Buttons to Control Frame
        self.button_show_oc = ttk.Button(self.control_frame, text="Show OC Curve", command=self.show_oc_curve)
        self.button_show_oc.pack(pady=5, fill='x')

        self.button_zoom_in_x = ttk.Button(self.control_frame, text="Zoom In X", command=self.zoom_in_x)
        self.button_zoom_in_x.pack(pady=5, fill='x')

        self.button_zoom_out_x = ttk.Button(self.control_frame, text="Zoom Out X", command=self.zoom_out_x)
        self.button_zoom_out_x.pack(pady=5, fill='x')

        self.button_shift_left = ttk.Button(self.control_frame, text="Shift Left", command=self.shift_left)
        self.button_shift_left.pack(pady=5, fill='x')

        self.button_shift_right = ttk.Button(self.control_frame, text="Shift Right", command=self.shift_right)
        self.button_shift_right.pack(pady=5, fill='x')

        self.button_reset_zoom = ttk.Button(self.control_frame, text="Reset Zoom", command=self.reset_zoom)
        self.button_reset_zoom.pack(pady=5, fill='x')

        self.button_save_plot = ttk.Button(self.control_frame, text="Save OC Curve", command=self.save_oc_curve)
        self.button_save_plot.pack(pady=5, fill='x')

    def calculate_pa(self, n, p, c):
        """
        Calculate the Probability of Acceptance (Pa) using the binomial distribution.
        """
        pa = 0
        for k in range(0, c + 1):
            pa += comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        return pa

    def show_oc_curve(self):
        """
        Generate and display the OC Curve based on input values.
        """
        try:
            n = self.input_frame.n
            c = self.input_frame.c

            if n is None or c is None:
                raise ValueError("กรุณากรอกข้อมูลใน InputFrame ก่อนแสดงกราฟ OC")

            # Create a range of p values from 0 to 1 with higher resolution
            p_values = [i / 10000 for i in range(0, 10001)]
            pa_values = [self.calculate_pa(n, p, c) for p in p_values]

            # Clear previous plots
            self.ax.clear()

            # Plot the OC Curve
            self.ax.plot(p_values, pa_values, label='OC Curve', color='blue')
            self.ax.set_title('Operating Characteristic (OC) Curve', fontsize=14)
            self.ax.set_xlabel('p: Fraction Defective', fontsize=12)
            self.ax.set_ylabel('Pa: Probability of Acceptance', fontsize=12)
            self.ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            self.ax.legend(fontsize=12)
            self.ax.tick_params(axis='both', which='major', labelsize=10)

            # Set initial limits
            self.current_xlim = self.initial_xlim
            self.current_ylim = self.initial_ylim
            self.ax.set_xlim(self.current_xlim)
            self.ax.set_ylim(self.current_ylim)

            # Improve layout
            self.fig.tight_layout()

            # Embed the plot in Tkinter
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def zoom_in_x(self):
        """
        Zoom in on the X-axis by decreasing the current limits by 0.05.
        """
        try:
            # Calculate new x-axis limits for zooming in by 0.05
            x_min, x_max = self.current_xlim
            zoom_step = 0.05

            # Calculate the amount to reduce from each side
            new_x_min = x_min + zoom_step / 2
            new_x_max = x_max - zoom_step / 2

            # Ensure limits do not exceed [0,1]
            new_x_min = max(0, new_x_min)
            new_x_max = min(1, new_x_max)

            # Update current limits
            self.current_xlim = (new_x_min, new_x_max)
            self.ax.set_xlim(self.current_xlim)
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def zoom_out_x(self):
        """
        Zoom out on the X-axis by increasing the current limits by 0.05.
        """
        try:
            # Calculate new x-axis limits for zooming out by 0.05
            x_min, x_max = self.current_xlim
            zoom_step = 0.05

            # Calculate the amount to add to each side
            new_x_min = x_min - zoom_step / 2
            new_x_max = x_max + zoom_step / 2

            # Ensure limits stay within [0,1]
            new_x_min = max(0, new_x_min)
            new_x_max = min(1, new_x_max)

            # Update current limits
            self.current_xlim = (new_x_min, new_x_max)
            self.ax.set_xlim(self.current_xlim)
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def shift_left(self):
        """
        Shift the X-axis interval to the left by 0.05.
        """
        try:
            x_min, x_max = self.current_xlim
            shift_step = 0.05

            new_x_min = x_min - shift_step
            new_x_max = x_max - shift_step

            # Ensure limits do not go below 0
            if new_x_min < 0:
                new_x_min = 0
                new_x_max = new_x_min + (x_max - x_min)

            self.current_xlim = (new_x_min, new_x_max)
            self.ax.set_xlim(self.current_xlim)
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def shift_right(self):
        """
        Shift the X-axis interval to the right by 0.05.
        """
        try:
            x_min, x_max = self.current_xlim
            shift_step = 0.05

            new_x_min = x_min + shift_step
            new_x_max = x_max + shift_step

            # Ensure limits do not exceed 1
            if new_x_max > 1:
                new_x_max = 1
                new_x_min = new_x_max - (x_max - x_min)

            self.current_xlim = (new_x_min, new_x_max)
            self.ax.set_xlim(self.current_xlim)
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reset_zoom(self):
        """
        Reset the X and Y axis limits to their initial values.
        """
        try:
            self.current_xlim = self.initial_xlim
            self.current_ylim = self.initial_ylim
            self.ax.set_xlim(self.current_xlim)
            self.ax.set_ylim(self.current_ylim)
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_oc_curve(self):
        """
        Save the current OC Curve plot as a PNG image.
        """
        try:
            if not self.canvas:
                raise ValueError("ไม่มีกราฟ OC Curve ที่จะแสดง กรุณาสร้างกราฟก่อน")

            # Ask user where to save the file
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("All files", "*.*")],
                                                     title="Save OC Curve")
            if file_path:
                self.fig.savefig(file_path)
                messagebox.showinfo("Success", f"OC Curve ถูกบันทึกเรียบร้อยแล้วที่:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
