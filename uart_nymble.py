import serial
import time

BAUD_RATE = 2400

def send_data(text, serial_port):
    ser = serial.Serial(serial_port, BAUD_RATE, timeout=1)

    for char in text:
        start_time = time.time() * 1e6  # Convert to microseconds
        ser.write(char.encode())
        end_time = time.time() * 1e6  # Convert to microseconds
        print_transmission_speed(end_time - start_time)

    ser.close()

def receive_data(serial_port):
    #ser = serial.Serial(serial_port, BAUD_RATE, timeout=1)
    ser = serial.Serial(serial_port, BAUD_RATE, timeout=1)

    received_data = ""
    while True:
        start_time = time.time() * 1e6  # Convert to microseconds
        char = ser.read().decode()
        end_time = time.time() * 1e6  # Convert to microseconds
        print_transmission_speed(end_time - start_time)

        if not char:
            break

        received_data += char

    ser.close()
    return received_data

def print_transmission_speed(duration):
    # Calculate and print real-time transmission speed in bits/second
    speed = 8.0 / (duration / 1e6)
    print(f"Speed: {speed:.2f} bits/second")

if __name__ == "__main__":
    text = """Your text goes here"""
    serial_port = "COM5"  # Adjust with your actual serial port

    send_data(text, serial_port)
    received_data = receive_data(serial_port)
    print("\nReceived Data:")
    print(received_data)
