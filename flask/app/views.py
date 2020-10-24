from app import app
import serial.tools.list_ports

@app.route("/")
def index():
    plist = list(serial.tools.list_ports.comports())
    print('list of serial ports...')
    print(plist)
    return "index"