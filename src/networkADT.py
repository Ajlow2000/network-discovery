import ipaddress
import json

from deviceADT import Device

class Network:
    """ADT to represent a network and relevant info"""

    def __init__(self, cidr):
        try:
            self.cidr = cidr
            self.address_range = [str(ip) for ip in ipaddress.IPv4Network(cidr)]
            self.active_hosts = {}
            self.scan_info = {}
        except ipaddress.AddressValueError:
            print("Provided value for cidr not a valid IPv4Network")

    def add_device(self, ip: ipaddress.IPv4Address, mac=None, tcp_port_results=None):
        self.active_hosts[ip] = Device(ip, mac, tcp_port_results)

    def log_scan(self, scan_type, time_elapsed, time_completed):
        self.scan_info[scan_type] = {}
        self.scan_info[scan_type]["time_elapsed"] = time_elapsed
        self.scan_info[scan_type]["time_completed"] = time_completed

    def to_dict(self):
        net_dict = {}
        net_dict["cidr"] = str(self.cidr)
        net_dict["active_hosts"] = {}
        for device_ip in sorted(self.active_hosts):
            net_dict["active_hosts"][device_ip] = self.active_hosts[device_ip].to_dict()
        net_dict["scan_info"] = self.scan_info
        return net_dict

    def json(self):
        return json.dumps(self.to_dict(), indent=4)
