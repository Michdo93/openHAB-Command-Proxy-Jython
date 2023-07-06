import time
import core
from core.rules import rule
from core.triggers import when
from flask import Flask, request

class OpenHABCommandProxy:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.app = Flask(__name__)
        self.register_routes()

    def register_routes(self):
        self.app.route('/rest/items/<item_name>', methods=['GET'])(self.handle_item_command)

    def handle_item_command(self, item_name):
        command = request.args.get('data')

        events.sendCommand(item_name, command)

        time.sleep(1)

        # Aktuellen Zustand abrufen
        current_state = ir.getItem(item_name).state

        if current_state == command:
            return 'Command received and processed', 200
        else:
            return 'Error: Command not processed', 500

    def run(self):
        self.app.run(host=self.ip_address, port=self.port)

@rule("Flask API")
@when("System started")
def start_flask_api(event):
    openHABCommandProxy = OpenHABCommandProxy("0.0.0.0", 12345)
    openHABCommandProxy.run()
