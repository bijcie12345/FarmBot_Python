from app import app
import serial
import time

@app.route("/")
def index():
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.5
    )
    return ser.isOpen()

@app.route("/move1")
def move():
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.5
    )

    input = 'G0 X400 F1000'
    ser.write(bytes(input + '\r\n', 'UTF-8'))
    out =''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode("utf-8")
        if out !='':
            print(">>" + out)
    ser.close()
    return "moved 1"

@app.route("/move2")
def move1():
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.5
    )

    input = 'G0 X100 F1000'
    ser.write(bytes(input + '\r\n', 'UTF-8'))
    out =''
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1).decode("utf-8")
        if out !='':
            print(">>" + out)
    ser.close()
    return "moved 2"