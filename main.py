import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
import time
import csv

# Data storage
altitude_data = []
pressure_data = []
temperature_data = []
voltage_data = []
time_data = []

# Simulation mode flag
simulation_mode = False

# Function to update the graphs
def update_graphs(i):
    global altitude_data, pressure_data, temperature_data, voltage_data, time_data

    # Clear previous plots
    for ax in axes:
        ax.clear()

    # Plot Altitude
    axes[0].plot(time_data, altitude_data, label='Altitude', color='blue')
    axes[0].set_title('Altitude')
    axes[0].set_xlabel('Time (s)')
    axes[0].set_ylabel('Altitude (m)')

    # Plot Pressure
    axes[1].plot(time_data, pressure_data, label='Pressure', color='green')
    axes[1].set_title('Pressure')
    axes[1].set_xlabel('Time (s)')
    axes[1].set_ylabel('Pressure (Pa)')

    # Plot Temperature
    axes[2].plot(time_data, temperature_data, label='Temperature', color='red')
    axes[2].set_title('Temperature')
    axes[2].set_xlabel('Time (s)')
    axes[2].set_ylabel('Temperature (°C)')

    # Plot Voltage
    axes[3].plot(time_data, voltage_data, label='Voltage', color='purple')
    axes[3].set_title('Voltage')
    axes[3].set_xlabel('Time (s)')
    axes[3].set_ylabel('Voltage (V)')

# Function to append new data (simulated or real)
def append_data(altitude, pressure, temperature, voltage):
    current_time = time.time() - start_time
    time_data.append(current_time)
    altitude_data.append(altitude)
    pressure_data.append(pressure)
    temperature_data.append(temperature)
    voltage_data.append(voltage)

# Function to handle mode selection
def set_mode(simulation, root):
    global simulation_mode, start_time
    simulation_mode = simulation
    root.destroy()
    start_time = time.time()
    ani = FuncAnimation(fig, update_graphs, interval=1000)
    plt.tight_layout()
    plt.show()

# Main interface using Tkinter
def main():
    root = tk.Tk()
    root.title("CanSat Interface")

    frame_left = ttk.Frame(root)
    frame_left.pack(side='left', fill='y')

    frame_right = ttk.Frame(root)
    frame_right.pack(side='right', expand=True, fill='both')

    tabs = ttk.Notebook(frame_left)
    tabs.pack(pady=10, padx=10)

    tab_graphs = ttk.Frame(tabs)
    tab_map = ttk.Frame(tabs)
    tab_telemetry = ttk.Frame(tabs)
    tab_simulation = ttk.Frame(tabs)

    tabs.add(tab_graphs, text='GRAPHS')
    tabs.add(tab_map, text='MAP')
    tabs.add(tab_telemetry, text='TELEMETRY')
    tabs.add(tab_simulation, text='SIMULATION')

    # Placeholder for graph area in the tab
    fig, axes = plt.subplots(2, 2, figsize=(8, 6))
    axes = axes.flatten()
    canvas = FigureCanvasTkAgg(fig, master=tab_graphs)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Commands Section
    ttk.Label(frame_left, text="Commands").pack(pady=10)
    commands = ['ST', 'CAL', 'CX ON', 'CX OFF', 'BCN ON', 'BCN OFF', 'CHUTE ⏷', 'CHUTE ⏶', 'HTSHLD ⏷', 'HTSHLD ⏶']
    for cmd in commands:
        ttk.Button(frame_left, text=cmd).pack(pady=2)

    # Simulation mode button
    ttk.Button(frame_left, text="Simulation Mode", command=lambda: set_mode(True, root)).pack(pady=10)
    ttk.Button(frame_left, text="Flight Mode", command=lambda: set_mode(False, root)).pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
