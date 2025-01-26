import tkinter as tk
from tkinter import ttk, filedialog
import csv
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to open telemetry page
def open_telemetry():
    clear_main_frame()

    telemetry_label = tk.Label(main_frame, text="Telemetry Data", font=("Arial", 20), fg="#333", bg="white")
    telemetry_label.pack(pady=10)

    telemetry_frame = tk.Frame(main_frame, bg="white")
    telemetry_frame.pack(fill="both", expand=True, padx=20, pady=10)

    left_table = ttk.Treeview(telemetry_frame, columns=("NAME", "VALUE"), show="headings", height=10)
    left_table.heading("NAME", text="NAME")
    left_table.heading("VALUE", text="VALUE")
    left_table.column("NAME", width=150)
    left_table.column("VALUE", width=100)
    left_table.grid(row=0, column=0, padx=10)

    right_table = ttk.Treeview(telemetry_frame, columns=("NAME", "VALUE"), show="headings", height=10)
    right_table.heading("NAME", text="NAME")
    right_table.heading("VALUE", text="VALUE")
    right_table.column("NAME", width=150)
    right_table.column("VALUE", width=100)
    right_table.grid(row=0, column=1, padx=10)

    # Example telemetry data
    left_data = [
        ("TEAM_ID", "2050"),
        ("MISSION_TIME", "15:24:09"),
        ("PACKET_COUNT", "00015"),
        ("MODE", "F"),
        ("STATE", "LAUNCH_WAIT"),
        ("ALTITUDE [m]", "0.0"),
        ("AIR_SPEED [m/s]", "2.9"),
        ("HS_DEPLOYED", "N"),
        ("PC_DEPLOYED", "N"),
        ("TEMPERATURE [°C]", "26.5"),
    ]

    right_data = [
        ("PRESSURE [kPa]", "102.5"),
        ("VOLTAGE [V]", "4.30"),
        ("GPS_TIME", "15:24:09"),
        ("GPS_ALTITUDE [m]", "110.6"),
        ("GPS_LATITUDE [°]", "34.2000"),
        ("GPS_LONGITUDE [°]", "-69.0000"),
        ("GPS_SATS", "3"),
        ("TILT_X [°]", "0.12"),
        ("TILT_Y [°]", "0.19"),
        ("ROT_Z [°/s]", "0.11"),
    ]

    for item in left_data:
        left_table.insert("", "end", values=item)

    for item in right_data:
        right_table.insert("", "end", values=item)

    packets_label = tk.Label(main_frame, text="Received packets: 26", font=("Arial", 14), fg="#333", bg="white")
    packets_label.pack(pady=10)

# Function to open graphs page
def open_graphs():
    clear_main_frame()

    graphs_label = tk.Label(main_frame, text="Graphs", font=("Arial", 20), fg="#333", bg="white")
    graphs_label.pack(pady=10)

    graphs_frame = tk.Frame(main_frame, bg="white")
    graphs_frame.pack(fill="both", expand=True, padx=20, pady=10)

    fig = Figure(figsize=(10, 4), dpi=100)
    altitude_plot = fig.add_subplot(221)
    altitude_plot.plot([700, 750, 800, 850, 825], label="Altitude")
    altitude_plot.set_title("Altitude")

    pressure_plot = fig.add_subplot(222)
    pressure_plot.plot([1010, 1015, 1020, 1025, 1030], label="Pressure")
    pressure_plot.set_title("Pressure")

    temperature_plot = fig.add_subplot(223)
    temperature_plot.plot([25, 26, 27, 28, 29], label="Temperature")
    temperature_plot.set_title("Temperature")

    velocity_plot = fig.add_subplot(224)
    velocity_plot.plot([5, 10, 15, 20, 25], label="Velocity")
    velocity_plot.set_title("Velocity")

    canvas = FigureCanvasTkAgg(fig, master=graphs_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Function to open simulation page
def open_simulation():
    clear_main_frame()

    simulation_label = tk.Label(main_frame, text="Simulation Mode", font=("Arial", 20), fg="#333", bg="white")
    simulation_label.pack(pady=10)

    # Create a frame for inputs
    input_frame = tk.Frame(main_frame, bg="white", pady=10)
    input_frame.pack(fill="x", padx=20)

    # Create a frame for graphs
    graph_frame = tk.Frame(main_frame, bg="white")
    graph_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Initialize lists for storing data
    altitudes = []
    pressures = []
    temperatures = []
    velocities = []

    def update_graphs():
        """Update the graphs in the graph frame."""
        for widget in graph_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(10, 8), dpi=100)

        # Altitude Plot
        altitude_plot = fig.add_subplot(221)
        altitude_plot.plot(altitudes, marker="o", label="Altitude")
        altitude_plot.set_title("Altitude")
        altitude_plot.set_xlabel("Data Set")
        altitude_plot.set_ylabel("Altitude [m]")

        # Pressure Plot
        pressure_plot = fig.add_subplot(222)
        pressure_plot.plot(pressures, marker="o", label="Pressure")
        pressure_plot.set_title("Pressure")
        pressure_plot.set_xlabel("Data Set")
        pressure_plot.set_ylabel("Pressure [kPa]")

        # Temperature Plot
        temperature_plot = fig.add_subplot(223)
        temperature_plot.plot(temperatures, marker="o", label="Temperature")
        temperature_plot.set_title("Temperature")
        temperature_plot.set_xlabel("Data Set")
        temperature_plot.set_ylabel("Temperature [°C]")

        # Velocity Plot
        velocity_plot = fig.add_subplot(224)
        velocity_plot.plot(velocities, marker="o", label="Velocity")
        velocity_plot.set_title("Velocity")
        velocity_plot.set_xlabel("Data Set")
        velocity_plot.set_ylabel("Velocity [m/s]")

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Functions to add data for each graph
    def add_altitude_data():
        try:
            altitude = float(altitude_entry.get())
            altitudes.append(altitude)
            altitude_entry.delete(0, tk.END)
            update_graphs()
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter a valid numerical value for Altitude.")

    def add_pressure_data():
        try:
            pressure = float(pressure_entry.get())
            pressures.append(pressure)
            pressure_entry.delete(0, tk.END)
            update_graphs()
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter a valid numerical value for Pressure.")

    def add_temperature_data():
        try:
            temperature = float(temperature_entry.get())
            temperatures.append(temperature)
            temperature_entry.delete(0, tk.END)
            update_graphs()
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter a valid numerical value for Temperature.")

    def add_velocity_data():
        try:
            velocity = float(velocity_entry.get())
            velocities.append(velocity)
            velocity_entry.delete(0, tk.END)
            update_graphs()
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter a valid numerical value for Velocity.")

    # Entry fields for each graph's data
    altitude_label = tk.Label(input_frame, text="Altitude [m]:", bg="white")
    altitude_label.grid(row=0, column=0, sticky="e")
    altitude_entry = tk.Entry(input_frame, width=20)
    altitude_entry.grid(row=0, column=1)

    pressure_label = tk.Label(input_frame, text="Pressure [kPa]:", bg="white")
    pressure_label.grid(row=1, column=0, sticky="e")
    pressure_entry = tk.Entry(input_frame, width=20)
    pressure_entry.grid(row=1, column=1)

    temperature_label = tk.Label(input_frame, text="Temperature [°C]:", bg="white")
    temperature_label.grid(row=2, column=0, sticky="e")
    temperature_entry = tk.Entry(input_frame, width=20)
    temperature_entry.grid(row=2, column=1)

    velocity_label = tk.Label(input_frame, text="Velocity [m/s]:", bg="white")
    velocity_label.grid(row=3, column=0, sticky="e")
    velocity_entry = tk.Entry(input_frame, width=20)
    velocity_entry.grid(row=3, column=1)

    # Buttons to add data for each graph
    add_altitude_button = tk.Button(input_frame, text="Add Altitude Data", bg="#3b82f6", fg="white", relief="flat", command=add_altitude_data)
    add_altitude_button.grid(row=0, column=2, padx=10)

    add_pressure_button = tk.Button(input_frame, text="Add Pressure Data", bg="#3b82f6", fg="white", relief="flat", command=add_pressure_data)
    add_pressure_button.grid(row=1, column=2, padx=10)

    add_temperature_button = tk.Button(input_frame, text="Add Temperature Data", bg="#3b82f6", fg="white", relief="flat", command=add_temperature_data)
    add_temperature_button.grid(row=2, column=2, padx=10)

    add_velocity_button = tk.Button(input_frame, text="Add Velocity Data", bg="#3b82f6", fg="white", relief="flat", command=add_velocity_data)
    add_velocity_button.grid(row=3, column=2, padx=10)

    # Initialize with empty graphs
    update_graphs()





# Function to upload a CSV file
def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)  # Process CSV data as needed

# Function to clear the main frame
def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Main Tkinter setup
root = tk.Tk()
root.title("CanSat 2024 Ground Station")
root.geometry("1200x800")
root.configure(bg="#f4f4f4")

# Header Frame
header_frame = tk.Frame(root, bg="#3b82f6", height=80)
header_frame.pack(fill="x", side="top")

header_label = tk.Label(header_frame, text="KoNaR CAN INTO SPACE", bg="#3b82f6", fg="white", font=("Arial", 20, "bold"))
header_label.pack(side="left", padx=20, pady=20)

status_label = tk.Label(header_frame, text="TEAM ID: 2050   MISSION TIME: 00:00:00.00", bg="#3b82f6", fg="white", font=("Arial", 14))
status_label.pack(side="right", padx=20, pady=20)

# Sidebar
side_frame = tk.Frame(root, bg="#e6e6e6", width=200)
side_frame.pack(fill="y", side="left")

buttons = [
    ("GRAPHS", open_graphs),
    ("MAP", None),
    ("TELEMETRY", open_telemetry),
    ("SIMULATION", open_simulation),
]

for text, command in buttons:
    tk.Button(side_frame, text=text, font=("Arial", 12), bg="#d0d0d0", relief="flat", command=command).pack(fill="x", pady=5, padx=10)

commands_label = tk.Label(side_frame, text="Commands", bg="#e6e6e6", font=("Arial", 14, "bold"))
commands_label.pack(pady=20)

for cmd in ["ST", "CAL", "CX ON", "CX OFF", "AUDIO"]:
    tk.Button(side_frame, text=cmd, font=("Arial", 12), bg="#d0d0d0", relief="flat").pack(fill="x", pady=5, padx=10)

# Main Frame
main_frame = tk.Frame(root, bg="white", padx=10, pady=10)
main_frame.pack(fill="both", expand=True, side="left")

root.mainloop()
