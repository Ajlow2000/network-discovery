import ipaddress
from datetime import datetime

class Device:
    """Object representing a networked device"""
    def __init__(self, ip, hostname=None, mac=None, tcp_port_results=None):
        try:
            self.ip = ipaddress.ip_address(ip)
            self.hostname = hostname
            self.mac = mac
            self.tcp_port_results = tcp_port_results
            self.time_last_updated = datetime.now()
        except ValueError:
            raise ValueError("Provided value for ip arg is not a valid ip_address")

    def update_time(self):
        self.time_last_updated = datetime.now()

    def to_dict(self):
        device_dict = {}
        device_dict["ip"] = str(self.ip)
        device_dict["hostname"] = str(self.hostname)
        device_dict["mac"] = str(self.mac)
        device_dict["tcp_port_results"] = {}
        if self.tcp_port_results is not None:
            for key in self.tcp_port_results:
                device_dict["tcp_port_results"][key] = str(self.tcp_port_results[key])
        device_dict["time_last_updated"] = str(self.time_last_updated)
        return device_dict