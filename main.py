import serial

def main():
    ser = serial.Serial("COM3", 9600, timeout=1)
    
    while True:
        tx = input("> ")
            
        if tx == "quit":
            break

        ser.write(tx.encode("utf-8"))
        rx = ser.readline().decode("utf-8")
        print(rx)

    ser.close()


if __name__ == "__main__":
    main()
