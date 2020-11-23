import ipaddress
import platform
import subprocess
import socket
from datetime import datetime

from deviceADT import Device
from networkADT import Network

class Pingsweep:
    """Tool for detecting listening devices on a single network"""

    def __init__(self, network: Network, outfile=None):
        self.detect_ping_cmd()
        self.network = network

    def detect_ping_cmd(self):
        cmd = {}
        cmd["linux"] = "ping -c 1 "
        cmd["windows"] = "ping -n 1 -w 500 "
        os = platform.system().lower()
        self.ping_cmd = cmd[os]

    def ping_ip(self, ip, STDOUT):
        try:
            result = subprocess.check_output(self.ping_cmd + str(ip), shell=True).decode()
            if "unreachable" or "Sent = 1, Received = 0" not in result:
                if STDOUT: print("\t" + ip)
                self.network.active_hosts[ip] = Device(ip, hostname=socket.gethostbyaddr(ip))
        except subprocess.CalledProcessError as e:
            pass
        except socket.herror as e: # TODO - Research this error
            pass

    def initialize(self, STDOUT=False):
        time_began = datetime.now()
        try:
            if STDOUT: print("Pingsweep Initialized")
            for ip in self.network.address_range:
                self.ping_ip(ip, STDOUT)
        except KeyboardInterrupt:
            pass
        finally:
            time_finished = datetime.now()
            self.network.log_scan("pingsweep", str(time_finished - time_began), str(time_finished))
            if STDOUT: print("Time Elapsed: " + str(time_finished - time_began) +"\n")
            return self.network