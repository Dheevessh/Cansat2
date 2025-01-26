import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv

def update_graphs():
    if not simulation_active:
        axs[0].clear()
        axs[0].plot(altitude_data, color="blue")
        axs[0].set_title("Altitude")
        axs[0].set_ylabel("Altitude (m)")
        axs[0].set_xlabel("Time")

        axs[1].clear()
        axs[1].plot(pressure_data, color="red")
        axs[1].set_title("Pressure")
        axs[1].set_ylabel("Pressure (hPa)")
        axs[1].set_xlabel("Time")

        axs[2].clear()
        axs[2].plot(velocity_data, color="green")
        axs[2].set_title("Velocity")
        axs[2].set_ylabel("Velocity (m/s)")
        axs[2].set_xlabel("Time")

        axs[3].clear()
        axs[3].plot(temperature_data, color="orange")
        axs[3].set_title("Temperature")
        axs[3].set_ylabel("Temperature (°C)")
        axs[3].set_xlabel("Time")

        canvas.draw()

def enable_simulation_mode():
    global simulation_active
    simulation_active = True

    simulation_frame.pack(fill="x", pady=10)  # Show the simulation frame
    graph_frame.pack_forget()  # Hide the graph frame

    for widget in simulation_frame.winfo_children():
        widget.configure(state="normal")

    update_simulation_graphs()

def show_graphs_page():
    global simulation_active
    simulation_active = False

    simulation_frame.pack_forget()  # Hide the simulation frame
    graph_frame.pack(fill="both", expand=True)  # Show the graph frame
    update_graphs()

def update_simulation_graphs():
    if simulation_active:
        axs[0].clear()
        axs[0].plot(sim_altitude_data, color="blue")
        axs[0].set_title("Altitude")
        axs[0].set_ylabel("Altitude (m)")
        axs[0].set_xlabel("Time")

        axs[1].clear()
        axs[1].plot(sim_pressure_data, color="red")
        axs[1].set_title("Pressure")
        axs[1].set_ylabel("Pressure (hPa)")
        axs[1].set_xlabel("Time")

        axs[2].clear()
        axs[2].plot(sim_velocity_data, color="green")
        axs[2].set_title("Velocity")
        axs[2].set_ylabel("Velocity (m/s)")
        axs[2].set_xlabel("Time")

        axs[3].clear()
        axs[3].plot(sim_temperature_data, color="orange")
        axs[3].set_title("Temperature")
        axs[3].set_ylabel("Temperature (°C)")
        axs[3].set_xlabel("Time")

        canvas.draw()

def load_csv_for_simulation():
    try:
        file_path = filedialog.askopenfilename(filetypes=[["CSV files", "*.csv"]])
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            sim_altitude_data.clear()
            sim_pressure_data.clear()
            sim_velocity_data.clear()
            sim_temperature_data.clear()
            for row in reader:
                sim_altitude_data.append(float(row[0]))
                sim_pressure_data.append(float(row[1]))
                sim_velocity_data.append(float(row[2]))
                sim_temperature_data.append(float(row[3]))
            update_simulation_graphs()
    except Exception as e:
        print("Error loading CSV:", e)

root = tk.Tk()
root.title("CanSat 2024 Ground Station")
root.geometry("1200x800")
root.configure(bg="#f4f4f4")

altitude_data = []
pressure_data = []
velocity_data = []
temperature_data = []

sim_altitude_data, sim_pressure_data, sim_velocity_data, sim_temperature_data = [], [], [], []
simulation_active = False

header_frame = tk.Frame(root, bg="#3b82f6", height=80)
header_frame.pack(fill="x", side="top")

header_label = tk.Label(header_frame, text="Aeroze", bg="#3b82f6", fg="white", font=("Arial", 20, "bold"))
header_label.pack(side="left", padx=20, pady=20)

status_label = tk.Label(header_frame, text="Connected", bg="#3b82f6", fg="green", font=("Arial", 14))
status_label.pack(side="right", padx=20, pady=20)

side_frame = tk.Frame(root, bg="#e6e6e6", width=200)
side_frame.pack(fill="y", side="left")

tabs_label = tk.Label(side_frame, text="Tabs", bg="#e6e6e6", font=("Arial", 14, "bold"))
tabs_label.pack(pady=10)

tk.Button(side_frame, text="GRAPHS", font=("Arial", 12), bg="#d0d0d0", relief="flat", command=show_graphs_page).pack(fill="x", pady=5, padx=10)
tk.Button(side_frame, text="MAP", font=("Arial", 12), bg="#d0d0d0", relief="flat").pack(fill="x", pady=5, padx=10)
tk.Button(side_frame, text="TELEMETRY", font=("Arial", 12), bg="#d0d0d0", relief="flat").pack(fill="x", pady=5, padx=10)
tk.Button(side_frame, text="SIMULATION", font=("Arial", 12), bg="#d0d0d0", relief="flat", command=enable_simulation_mode).pack(fill="x", pady=5, padx=10)

commands_label = tk.Label(side_frame, text="Commands", bg="#e6e6e6", font=("Arial", 14, "bold"))
commands_label.pack(pady=20)

for cmd in ["ST", "CAL", "CX ON", "CX OFF", "AUDIO"]:
    tk.Button(side_frame, text=cmd, font=("Arial", 12), bg="#d0d0d0", relief="flat").pack(fill="x", pady=5, padx=10)

main_frame = tk.Frame(root, bg="white", padx=10, pady=10)
main_frame.pack(fill="both", expand=True, side="left")

fig, axs = plt.subplots(2, 2, figsize=(10, 6))
axs = axs.flatten()

canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill="both", expand=True)

simulation_frame = tk.Frame(side_frame, bg="#e6e6e6")
simulation_frame.grid_columnconfigure(0, weight=1)
simulation_frame.pack_forget()  # Hide the simulation frame by default

root.mainloop()
