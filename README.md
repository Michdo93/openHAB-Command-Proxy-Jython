# openHAB-Command-Proxy-Jython
A Jython script with Flask that provides a REST API for commands to an openHAB item, so that you can execute a sendCommand via GET request.

## Installation

At first you have to install following dependencies:

```
sudo -u openhab python3 -m pip install flask --user
```

Then you can download the python script with:

```
git clone https://github.com/Michdo93/openHAB-Command-Proxy-Jython.git $OH_CONF/automation/jsr223/python/community
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

## Example Use Case

A simple use case would be to scan QR codes that can be used to operate devices. A commercially available QR code scanner suggests that if a URL is recognised, it can be opened in the browser. However, in order to perform a sendCommand on an item in openHAB, a POST request must be performed, whereas opening a URL in the browser is only a GET request.

<div>
    <img src="https://raw.githubusercontent.com/Michdo93/test2/main/qr_scan_openhab.png" alt="QR 1" width="300" />
    <img src="https://raw.githubusercontent.com/Michdo93/test2/main/qr_scan_openhab2.png" alt="QR 2" width="300" />
    <img src="https://raw.githubusercontent.com/Michdo93/test2/main/qr_scan_openhab3.png" alt="QR 3" width="300" />
</div>
