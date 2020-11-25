import json
from networkADT import Network
from net_tools import scan

n = Network("192.168.50.0/24")
n = scan(n)
print(n.json())