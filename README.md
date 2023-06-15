# openHAB-Command-Proxy
Send a command as a GET request to this REST API developed with Python and Flask for an openHAB item and it forwards this as a POST request to the REST API of openHAB.

## Installation

At first you have to install following dependencies:

```
python3 -m pip install python-openhab-crud
python3 -m pip install flask
```

Then you can download the python script with:

```
wget https://raw.githubusercontent.com/Michdo93/openHAB-Command-Proxy/main/openhab_command_proxy.py
sudo chmod +x openhab_command_proxy.py
```

Before you run the script, please adjust the following line:

```
app = OpenHABCommandProxy("<flask_ip>", <flask_port>, "<openhab_protocol>", "<openhab_ip>", <openhab_port>)
```

Replace the `"<flask_ip>"` with the IP address on which you want to run the proxy. You can freely select the port for the proxy with `<flask_port>`. Please note, however, that if you generate QR codes, for example, you should not keep changing the port so that the QR code can still point to the correct URL. Replace `"<openhab_protocol>"` with `"http"` or `"https"` depending on the installation. Replace `"<openhab_ip>"` with the IP address of the server you are running openHAB on. This may be the same IP address as the proxy. At the end you should adjust the `<openhab_port>`. By default, `8080` is used for this.

If you want to use the proxy on the same server as where you installed openHAB, download the following file:

```
wget https://raw.githubusercontent.com/Michdo93/openHAB-Command-Proxy/main/openhab-command-proxy.service
sudo mv openhab-command-proxy.service /etc/systemd/system
```

If you want to use the proxy on another server, download the following file:

```
wget https://raw.githubusercontent.com/Michdo93/openHAB-Command-Proxy/main/openhab-command-proxy2.service
sudo mv openhab-command-proxy2.service openhab-command-proxy.service
sudo mv openhab-command-proxy.service /etc/systemd/system
```

Please replace `<user>` with your username of the server!

At least you can start it by running:

```
sudo systemctl start openhab-command-proxy.service
```

If you want it to run after boot you have to enter:

```
sudo systemctl enable openhab-command-proxy.service
```

You can check the status with:

```
sudo systemctl status openhab-command-proxy.service
```

You can stop it with:

```
sudo systemctl stop openhab-command-proxy.service
```

If you want to disable running this proxy after boot you should run:

```
sudo systemctl disable openhab-command-proxy.service
```

## Example Use Case

A simple use case would be to scan QR codes that can be used to operate devices. A commercially available QR code scanner suggests that if a URL is recognised, it can be opened in the browser. However, in order to perform a sendCommand on an item in openHAB, a POST request must be performed, whereas opening a URL in the browser is only a GET request.

