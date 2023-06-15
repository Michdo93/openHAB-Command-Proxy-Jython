from flask import Flask, request
from openhab import CRUD

class OpenHABCommandProxy:
    def __init__(self, ip_address, port, openhab_protocol, openhab_ip, openhab_port):
        self.ip_address = ip_address
        self.port = port
        self.crud = CRUD(f"{openhab_protocol}://{openhab_ip}:{openhab_port}")

        self.app = Flask(__name__)
        self.register_routes()

    def register_routes(self):
        self.app.route('/rest/items/<item_name>', methods=['GET'])(self.handle_item_command)

    def handle_item_command(self, item_name):
        data = request.args.get('data')

        try:
            self.crud.sendCommand(item_name, data)
            # Hier können Sie weitere Aktionen durchführen, wenn der sendCommand erfolgreich war
            return 'Command received and processed', 200
        except Exception as e:
            # Hier können Sie weitere Aktionen durchführen, wenn ein Fehler aufgetreten ist
            print(f"Error while sending command: {str(e)}")
            return 'Error: Command not processed', 500

    def run(self):
        self.app.run(host=self.ip_address, port=self.port)

if __name__ == '__main__':
    ip = 
    app = OpenHABCommandProxy("<flask_ip>", <flask_port>, "<openhab_protocol>", "<openhab_ip>", <openhab_port>)
    app.run()
