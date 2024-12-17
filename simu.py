import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def simulate():
    try:
        # Fetch user inputs
        max_altitude = float(altitude_entry.get())
        max_temp = float(temperature_entry.get())
        min_pressure = float(pressure_entry.get())
        
        # Generate simulation data
        time = np.linspace(0, 100, 500)
        altitude = max_altitude * np.sin(np.pi * time / max(time))
        temperature = max_temp * np.cos(np.pi * time / max(time))
        pressure = min_pressure + (1013 - min_pressure) * np.sin(np.pi * time / max(time))
        
        # Clear and redraw graphs
        for ax in axs:
            ax.clear()

        axs[0].plot(time, altitude, label="Altitude (m)", color="blue")
        axs[0].set_title("Altitude vs Time")
        axs[0].set_xlabel("Time (s)")
        axs[0].set_ylabel("Altitude (m)")
        axs[0].legend()

        axs[1].plot(time, temperature, label="Temperature (°C)", color="red")
        axs[1].set_title("Temperature vs Time")
        axs[1].set_xlabel("Time (s)")
        axs[1].set_ylabel("Temperature (°C)")
        axs[1].legend()

        axs[2].plot(time, pressure, label="Pressure (hPa)", color="green")
        axs[2].set_title("Pressure vs Time")
        axs[2].set_xlabel("Time (s)")
        axs[2].set_ylabel("Pressure (hPa)")
        axs[2].legend()

        canvas.draw()

        # Update visual simulation
        update_visual_simulation(time, altitude)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")

def update_visual_simulation(time, altitude):
    visual_canvas.delete("all")
    width = visual_canvas.winfo_width()
    height = visual_canvas.winfo_height()

    for i in range(len(time)):
        x = int(width * time[i] / max(time))
        y = int(height - (height * altitude[i] / max(altitude)))
        visual_canvas.create_oval(x-5, y-5, x+5, y+5, fill="green", outline="")
        visual_canvas.update()
        visual_canvas.after(10)

# Create main window
root = tk.Tk()
root.title("Satellite Ascent and Descent Simulation")
root.geometry("1000x800")

# Input frame
input_frame = ttk.LabelFrame(root, text="Simulation Parameters")
input_frame.pack(fill="x", padx=10, pady=10)

# Input fields
altitude_label = ttk.Label(input_frame, text="Max Altitude (m):")
altitude_label.grid(row=0, column=0, padx=5, pady=5)
altitude_entry = ttk.Entry(input_frame)
altitude_entry.grid(row=0, column=1, padx=5, pady=5)

temperature_label = ttk.Label(input_frame, text="Max Temperature (°C):")
temperature_label.grid(row=1, column=0, padx=5, pady=5)
temperature_entry = ttk.Entry(input_frame)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

pressure_label = ttk.Label(input_frame, text="Min Pressure (hPa):")
pressure_label.grid(row=2, column=0, padx=5, pady=5)
pressure_entry = ttk.Entry(input_frame)
pressure_entry.grid(row=2, column=1, padx=5, pady=5)

simulate_button = ttk.Button(input_frame, text="Simulate", command=simulate)
simulate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Plotting area
fig, axs = plt.subplots(3, 1, figsize=(8, 10))
fig.tight_layout(pad=5.0)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill="both", expand=True, side="left")

# Visual simulation area
visual_frame = ttk.LabelFrame(root, text="Visual Simulation")
visual_frame.pack(fill="both", expand=True, side="right", padx=10, pady=10)

visual_canvas = tk.Canvas(visual_frame, bg="black")
visual_canvas.pack(fill="both", expand=True)

# Run the application
root.mainloop()
