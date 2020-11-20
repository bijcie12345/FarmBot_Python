import serial.tools.list_ports

def connect_serial_port() -> str:
    print("inside serial port")
    ports = list(serial.tools.list_ports.comports())
    a = 'porty '
    for p in ports:
        print(p)
        a += ','.join(map(str, p))
    return a
