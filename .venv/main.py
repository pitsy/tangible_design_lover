import serial
from src.serial_handler import read_from_arduino

prompt = "funny, 7 eyes, hairy, adventurous, lazy"

def main():
    # Setup serial connection
    ser = serial.Serial('COM6', 9600, timeout=1)  # Adjust according to your setup
    try:
        read_from_arduino(ser)
    finally:
        ser.close()

if __name__ == "__main__":
    main()
