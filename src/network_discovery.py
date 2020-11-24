from networkADT import Network
from pingsweep import Pingsweep

import json

test_network = Network("192.168.50.0/24")
ps = Pingsweep(test_network)
test_network = ps.initialize(STDOUT=True)
print(json.dumps(test_network.to_dict(), indent=4))