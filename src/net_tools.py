import platform
import socket
import subprocess
from datetime import datetime, time

from networkADT import Network

def pingsweep(network: Network, STDOUT=True):
    def detect_ping_cmd():
        cmd = {}
        cmd["linux"] = "ping -c 1 "
        cmd["windows"] = "ping -n 1 -w 500 "
        os = platform.system().lower()
        return cmd[os]

    def ping_ip(ip):
        try:
            result = subprocess.check_output(detect_ping_cmd() + str(ip), shell=True).decode()
            if "unreachable" or "Sent = 1, Received = 0" not in result:
                if STDOUT: print("\t" + ip)
                hostname = socket.gethostbyaddr(ip)[0]
                network.add_device(ip, hostname)
        except subprocess.CalledProcessError as e:
            pass
        except socket.herror as e: # TODO - Research this error
            pass

    try:
        ping_start = datetime.now()
        if STDOUT: print("Pingsweep Initialized")
        for ip in network.address_range:
            ping_ip(ip)
    except KeyboardInterrupt:
        if STDOUT: print("Cancelling...\n")
    finally:
        ping_end = datetime.now()
        ping_time = ping_end - ping_start
        network.log_scan("pingsweep", time_elapsed=str(ping_time), time_completed=str(ping_end))
        if STDOUT: print("Completed in " + str(ping_time))
        return network

def arpscan(network: Network, STDOUT=True):
    pass

def portscan(network: Network, ports, protocol="tcp", STDOUT=True):
    pass