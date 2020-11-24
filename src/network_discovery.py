from networkADT import Network
from net_tools import pingsweep, arpscan, portscan

def interactive():
    session_results = {}
    cidrs = input("Input Network CIDRs (comma separated): ").split(",")
    print("\nScan Types")
    print("\t[1] Pingsweep")
    print("\t[2] Arpscan")
    print("\t[3] Portscan")
    scan_type = input("Selection: ")
    if scan_type.lower() == "1" or "pingsweep":
        for cidr in cidrs:
            session_results[cidr] = pingsweep(Network(cidr))

def main():
    interactive()

main()