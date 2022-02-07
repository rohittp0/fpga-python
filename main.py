import serial


def main():
    ser = serial.Serial("COM4", timeout=None, baudrate=9600, xonxoff=False, rtscts=False, dsrdtr=False)
    try:
        ser.open()
    except serial.SerialException:
        pass

    print("Let's talk")

    while True:
        char = ser.read().decode()

        if char == "~":
            break

        print(char, end="")

    print("\nGood bye 👋")


if __name__ == '__main__':
    main()

