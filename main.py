import serial
import time

# Configuration for the XBee module connected to the laptop
SERIAL_PORT = 'COM3'  # Change to your XBee's serial port
BAUD_RATE = 9600  # Match the baud rate of the XBee modules

def main():
    try:
        # Establish serial connection
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print("Connected to XBee module on laptop.")
            
            while True:
                # Send "START" signal to CanSat
                command = input("Type 'start' to begin countdown or 'exit' to quit: ").strip().lower()
                if command == 'start':
                    ser.write(b'START\n')
                    print("Sent START signal. Waiting for data...")
                    
                    # Wait for data from CanSat
                    while True:
                        data = ser.readline().decode('utf-8').strip()
                        if data:
                            print(f"Received from CanSat: {data}")
                elif command == 'exit':
                    print("Exiting program.")
                    break
                else:
                    print("Invalid command. Type 'start' or 'exit'.")
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

if __name__ == '__main__':
    main()
