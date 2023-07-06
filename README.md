# openHAB-Command-Proxy-Jython
A Jython script with Flask that provides a REST API for commands to an openHAB item, so that you can execute a sendCommand via GET request.

The openHAB REST API would only allow you to perform a sendCommand with a POST request or a postUpdate with a PUT request. Using this proxy, you can also perform a sendCommand to an item via a GET request, which is e.g. calling up a URL in the browser. In Examples you can see that this can be useful, for example, for scanning a QR code.

This is a further development of [openHAB-Command-Proxy](https://github.com/Michdo93/openHAB-Command-Proxy).

## Installation

At first you have to install following dependencies:

```
sudo -u openhab python3 -m pip install flask --user
```

Then you can download the python script with:

```
git clone https://github.com/Michdo93/openHAB-Command-Proxy-Jython.git $OH_CONF/automation/jsr223/python/community/openHAB-Command-Proxy-Jython
```

Before you run the script, please make it executable:

```
sudo chown -R openhab:openhab $OH_CONF/automation/jsr223/python/community/openHAB-Command-Proxy-Jython/proxy.py
sudo chmod +x $OH_CONF/automation/jsr223/python/community/openHAB-Command-Proxy-Jython/proxy.py
```

At least you have to restart openhab:

```
sudo systemctl restart openhab
```

## Customization

You can change the port in following line (by default it is 12345):

```
openHABCommandProxy = OpenHABCommandProxy("0.0.0.0", 12345)
```

You do not need to change `"0.0.0.0"` as openHAB will run under the same IP address.

## Example Use Case

A simple use case would be to scan QR codes that can be used to operate devices. A commercially available QR code scanner suggests that if a URL is recognised, it can be opened in the browser. However, in order to perform a sendCommand on an item in openHAB, a POST request must be performed, whereas opening a URL in the browser is only a GET request.

<div>
    <img src="https://raw.githubusercontent.com/Michdo93/test2/main/qr_scan_openhab.png" alt="QR 1" width="300" />
    <img src="https://raw.githubusercontent.com/Michdo93/test2/main/qr_scan_openhab2.png" alt="QR 2" width="300" />
    <img src="https://raw.githubusercontent.com/Michdo93/test2/main/qr_scan_openhab3.png" alt="QR 3" width="300" />
</div>

Keep in mind that you have to use a different port for the QR code than for openHAB. If you have not configured a port for openHAB, it will use the default port `8080`. If the QR code were to contain the port `8080` accordingly, the openHAB server would report an error and not execute a sendCommand, as this is not possible with a GET request.
