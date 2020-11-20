from app import app
import os
from farmbot.configurations import serialPort

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"

@app.route("/dev", methods=['GET'])
def home():
    a = serialPort.connect_serial_port()
    return f"<h1>Distant reading archive</h1><p>This sitedsds is a prototpye API for ...</p> {a}"