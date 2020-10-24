from app import app as application
import serial.tools.list_ports

@application.route("/")
def index():
    plist = list(serial.tools.list_ports.comports())
    print('list of serial ports...')
    print(plist)
    return "index"