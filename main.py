import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Function to open the simulation mode in a new page
def open_simulation_mode():
    simulation_window = tk.Toplevel(root)
    simulation_window.title("Simulation Mode")
    simulation_window.geometry("1000x800")
    simulation_window.configure(bg="#f0f0f0")

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

            axs[0].plot(time, altitude, label="Altitude (m)", color="#4caf50", linewidth=2)
            axs[0].set_title("Altitude vs Time", fontsize=14, color="#4caf50")
            axs[0].set_xlabel("Time (s)", fontsize=12)
            axs[0].set_ylabel("Altitude (m)", fontsize=12)
            axs[0].legend()

            axs[1].plot(time, temperature, label="Temperature (\u00b0C)", color="#f44336", linewidth=2)
            axs[1].set_title("Temperature vs Time", fontsize=14, color="#f44336")
            axs[1].set_xlabel("Time (s)", fontsize=12)
            axs[1].set_ylabel("Temperature (\u00b0C)", fontsize=12)
            axs[1].legend()

            axs[2].plot(time, pressure, label="Pressure (hPa)", color="#2196f3", linewidth=2)
            axs[2].set_title("Pressure vs Time", fontsize=14, color="#2196f3")
            axs[2].set_xlabel("Time (s)", fontsize=12)
            axs[2].set_ylabel("Pressure (hPa)", fontsize=12)
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
            visual_canvas.create_oval(x-5, y-5, x+5, y+5, fill="#4caf50", outline="")
            visual_canvas.update()
            visual_canvas.after(5)

    # Input frame for simulation parameters
    input_frame = ttk.LabelFrame(simulation_window, text="Simulation Parameters", padding=(10, 10))
    input_frame.pack(fill="x", padx=10, pady=10)

    # Input fields
    altitude_label = ttk.Label(input_frame, text="Max Altitude (m):")
    altitude_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    altitude_entry = ttk.Entry(input_frame)
    altitude_entry.grid(row=0, column=1, padx=5, pady=5)

    temperature_label = ttk.Label(input_frame, text="Max Temperature (\u00b0C):")
    temperature_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    temperature_entry = ttk.Entry(input_frame)
    temperature_entry.grid(row=1, column=1, padx=5, pady=5)

    pressure_label = ttk.Label(input_frame, text="Min Pressure (hPa):")
    pressure_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    pressure_entry = ttk.Entry(input_frame)
    pressure_entry.grid(row=2, column=1, padx=5, pady=5)

    simulate_button = ttk.Button(input_frame, text="Simulate", command=simulate)
    simulate_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Plotting area
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))
    fig.patch.set_facecolor("#f0f0f0")
    fig.tight_layout(pad=5.0)

    canvas = FigureCanvasTkAgg(fig, master=simulation_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True, side="left", padx=10, pady=10)

    # Visual simulation area
    visual_frame = ttk.LabelFrame(simulation_window, text="Visual Simulation", padding=(10, 10))
    visual_frame.pack(fill="both", expand=True, side="right", padx=10, pady=10)

    visual_canvas = tk.Canvas(visual_frame, bg="#333333")
    visual_canvas.pack(fill="both", expand=True)

# Create main window
root = tk.Tk()
root.title("CanSat 2024 Ground Station")
root.geometry("800x600")

# Main frame
main_frame = ttk.Frame(root, padding=(10, 10))
main_frame.pack(fill="both", expand=True)

# Button to open simulation mode
simulation_button = ttk.Button(main_frame, text="Open Simulation Mode", command=open_simulation_mode)
simulation_button.pack(pady=20)

# Run the application
root.mainloop()
