import tkinter as tk
from tkinter import ttk, filedialog
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

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
    altitude_plot = fig.add_subplot(121)
    altitude_plot.plot([700, 750, 800, 850, 825], label="Altitude")
    altitude_plot.set_title("Altitude")

    pressure_plot = fig.add_subplot(122)
    pressure_plot.plot([1010, 1015, 1020, 1025, 1030], label="Pressure")
    pressure_plot.set_title("Pressure")

    canvas = FigureCanvasTkAgg(fig, master=graphs_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Function to open simulation page
# Update the simulation function to include a front page with buttons
def open_simulation():
    clear_main_frame()

    simulation_label = tk.Label(main_frame, text="SIMULATION", font=("Arial", 20), fg="#333", bg="white")
    simulation_label.pack(pady=10)

    # Front page layout
    front_page_frame = tk.Frame(main_frame, bg="white")
    front_page_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def activate_simulation_mode():
        front_page_frame.destroy()  # Clear the front page frame
        simulation_mode_page()  # Open simulation mode page

    # Buttons for "Enable", "Activate", "Disable"
    upload_button = tk.Button(front_page_frame, text="Upload CSV", bg="#d0d0d0", font=("Arial", 14), command=upload_csv)
    upload_button.pack(pady=10)

    enable_button = tk.Button(front_page_frame, text="ENABLE", bg="#c7d7fe", fg="#000", font=("Arial", 14))
    enable_button.pack(pady=10)

    activate_button = tk.Button(front_page_frame, text="ACTIVATE", bg="#c7d7fe", fg="#000", font=("Arial", 14),
                                command=activate_simulation_mode)
    activate_button.pack(pady=10)

    disable_button = tk.Button(front_page_frame, text="DISABLE", bg="#f77", fg="#000", font=("Arial", 14))
    disable_button.pack(pady=10)


# Simulation mode page where the user can add data
def simulation_mode_page():
    simulation_label = tk.Label(main_frame, text="Simulation Mode", font=("Arial", 20), fg="#333", bg="white")
    simulation_label.pack(pady=10)

    # Create a frame for inputs
    input_frame = tk.Frame(main_frame, bg="white", pady=10)
    input_frame.pack(fill="x", padx=20)

    # Create a frame for graphs
    graph_frame = tk.Frame(main_frame, bg="white")
    graph_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Initialize lists for storing data
    pressures = []
    altitudes = []

    def update_graphs():
        """Update the graphs in the graph frame."""
        for widget in graph_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(10, 4), dpi=100)

        # Pressure Plot
        pressure_plot = fig.add_subplot(121)
        pressure_plot.plot(pressures, marker="o", label="Pressure", color="blue")
        pressure_plot.set_title("Pressure")
        pressure_plot.set_xlabel("Data Set")
        pressure_plot.set_ylabel("Pressure [kPa]")

        # Altitude Plot (dependent on pressure values)
        altitude_plot = fig.add_subplot(122)
        altitude_plot.plot(altitudes, marker="o", label="Altitude", color="green")
        altitude_plot.set_title("Altitude")
        altitude_plot.set_xlabel("Data Set")
        altitude_plot.set_ylabel("Altitude [m]")

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def add_pressure_data():
        """Add pressure data and calculate altitude based on a simple formula."""
        try:
            pressure = float(pressure_entry.get())
            pressures.append(pressure)
            altitude = 44330 * (1 - (pressure / 1013.25) ** (1 / 5.255))  # Simplified barometric formula
            altitudes.append(altitude)
            pressure_entry.delete(0, tk.END)
            update_graphs()
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter a valid numerical value for Pressure.")

    # Entry fields for pressure data
    pressure_label = tk.Label(input_frame, text="Pressure [kPa]:", bg="white")
    pressure_label.grid(row=0, column=0, sticky="e")
    pressure_entry = tk.Entry(input_frame, width=20)
    pressure_entry.grid(row=0, column=1)

    # Button to add pressure data
    add_pressure_button = tk.Button(input_frame, text="Add Pressure Data", bg="#3b82f6", fg="white", relief="flat",
                                     command=add_pressure_data)
    add_pressure_button.grid(row=0, column=2, padx=10)

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
header_frame = tk.Frame(root, bg="#93c5fd", height=80)
header_frame.pack(fill="x", side="top")



# Load the Cansat logo image (replace "cansat_logo.png" with the actual file path)
cansat_logo_image = Image.open("cansat_logo.png")
cansat_logo_image = cansat_logo_image.resize((80, 80), Image.LANCZOS)  # Use LANCZOS for resizing
cansat_logo_photo = ImageTk.PhotoImage(cansat_logo_image)

# Add the logo to the left side
logo_label = tk.Label(header_frame, image=cansat_logo_photo, bg="#93c5fd")
logo_label.image = cansat_logo_photo  # Keep a reference to prevent garbage collection
logo_label.pack(side="left", padx=20, pady=20)  # Position the logo on the left

# Header Frame
header_label = tk.Label(header_frame, text="Aeroze", bg="#93c5fd", fg="white", font=("Arial", 20, "bold"))
header_label.pack(side="left", padx=10, pady=20)  # Position text on the right




status_label = tk.Label(header_frame, text="TEAM ID: 3160   MISSION TIME: 00:00:00.00", bg="#93c5fd", fg="white", font=("Arial", 14))
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
