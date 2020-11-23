import ipaddress
import json

class Network:
    """ADT to represent a network and relevant info"""

    def __init__(self, cidr):
        try:
            self.cidr = cidr
            self.address_range = [str(ip) for ip in ipaddress.IPv4Network(cidr)]
            self.active_hosts = {}
            self.scan_info = {}
        except ipaddress.NetmaskValueError:
            print("Provided value for cidr not a valid IPv4Network")

    def log_scan(self, scan_type, time_elapsed, time_completed):
        self.scan_info[scan_type] = {}
        self.scan_info[scan_type]["time_elapsed"] = time_elapsed
        self.scan_info[scan_type]["time_completed"] = time_completed

    def json(self):
        net_dict = {}
        net_dict["cidr"] = self.cidr
        net_dict["active_hosts"] = {}
        for device in sorted(self.active_hosts):
            pass # FIXME - Left off here
            # Question on how to access active host's devices

        return json.dumps(net_dict)
