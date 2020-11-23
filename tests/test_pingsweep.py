import unittest
import sys
import os
from unittest.main import main

SRC_PATH = str(os.getcwd()) + "/src/"
sys.path.append(SRC_PATH)

from pingsweep import Pingsweep


class TestPingsweep(unittest.TestCase):
    pass

    #def test_pingsweep_calculated_addresses(self):
        

main()
