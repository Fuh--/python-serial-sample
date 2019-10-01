import serial
import serial.tools.list_ports as list_ports

def main():
    ports = list(list_ports.comports())
    print('Please select a port:')
    p0arr = []
    p1arr = []
    for port in ports:
        print(port[1])
        p0arr.append(port[0])
        p1arr.append(port[1])
    selected = input()
    try:
        item = list(p0arr).index(selected)
    except ValueError:
        try:
            item = list(p1arr).index(selected)
        except ValueError:
            print('Port does not exist!')
            return
    selected_port = ports[item][0]
    ser = serial.Serial(selected_port, 9600, timeout=1)
    
    while True:
        tx = input("> ")
            
        if tx == "quit":
            ser.close()
            break

        ser.write(tx.encode("utf-8"))
        rx = ser.readline().decode("utf-8")
        print(rx)

    ser.close()


if __name__ == "__main__":
    main()
