from init_submodules import *

import unittest
import logging
import sys


class TestInitSubmodules(unittest.TestCase):
    def test_sh_escape(self):
        self.assertEqual(sh_escape("cd {}", "/; rm -rf /"), "cd '/; rm -rf /'")
        self.assertEqual(sh_escape("cd {} {}", 1, 2), "cd 1 2")


if __name__ == "__main__":
    unittest.main()
