import platform
import socket
import subprocess
from scapy.all import Ether, ARP, srp
from datetime import datetime, time

from networkADT import Network

def scan(network: Network, protocol="icmp", ports=None, STDOUT=True):

    def ping_ip(ip):
        def detect_ping_cmd():
            cmd = {}
            cmd["linux"] = "ping -c 1 "
            cmd["windows"] = "ping -n 1 -w 500 "
            os = platform.system().lower()
            return cmd[os]

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
        start = datetime.now()
        if STDOUT: print("Scan Initialized with " + protocol.upper())
        for ip in network.address_range:
            if protocol == "icmp":
                ping_ip(ip)
            elif protocol == "arp":
                arp_ip(ip)
            else:
                raise ValueError("Unrecognized Protocol: " + protocol)
    except KeyboardInterrupt:
        if STDOUT: print("Cancelling...\n")
    finally:
        end = datetime.now()
        elapsed = end - start 
        network.log_scan(protocol, time_elapsed=str(elapsed), time_completed=str(end))
        if STDOUT: print("Completed in " + str(elapsed))
        return network
