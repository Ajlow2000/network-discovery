import unittest
import sys
import os
from unittest.main import main

SRC_PATH = str(os.getcwd()) + "/src/"
sys.path.append(SRC_PATH)

from deviceADT import Device


class TestDevice(unittest.TestCase):

    def test_device_invalid_ip(self):
        with self.assertRaises(ValueError):
            Device("120.023.23", "h", "m", "tcp")

    def test_device_time_updates(self):
        d = Device("10.0.96.13", "foo", "mac", None)
        t1 = d.time_last_updated
        d.update_time()
        t2 = d.time_last_updated
        self.assertNotEqual(t1, t2)

    def test_device_default_time(self):
        d = Device("10.0.95.39", None, None, None)
        self.assertIsNotNone(d.time_last_updated)

main()