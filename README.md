# openHAB-Command-Proxy
Send a command as a GET request to this REST API developed with Python and Flask for an openHAB item and it forwards this as a POST request to the REST API of openHAB.

## Installation



## Example Use Case

A simple use case would be to scan QR codes that can be used to operate devices. A commercially available QR code scanner suggests that if a URL is recognised, it can be opened in the browser. However, in order to perform a sendCommand on an item in openHAB, a POST request must be performed, whereas opening a URL in the browser is only a GET request.
