#!/usr/bin/env python3

from configparser import ConfigParser
from subprocess import call
from shlex import quote
import unittest
import logging
import sys


class TestInitSubmodules(unittest.TestCase):
    def test_sh_escape(self):
        self.assertEqual(sh_escape("cd {}", "/; rm -rf /"), "cd '/; rm -rf /'")
        self.assertEqual(sh_escape("cd {} {}", 1, 2), "cd 1 2")
        self.assertEqual(sh_escape("cd {} {}", "/* asdf", 2), "cd '/* asdf' 2")


def sh_escape(cmd, *args):
    return cmd.format(*list(map(quote, map(str, args))))


def sh(cmd, *args):
    try:
        cmd = sh_escape(cmd, *args)
        print(f"+ {cmd}")
        r = call(cmd, shell=True)
        if r != 0:
            __import__("sys").exit(r)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestInitSubmodules("test_sh_escape"))
    unittest.TextTestRunner().run(suite)
    sh("git submodule update --init --recursive")
    c = ConfigParser()
    c.read(".gitmodules")
    for s in c.sections():
        p = c[s]["path"]
        try:
            b = c[s]["branch"]
        except:
            continue
        sh("cd {} && git checkout {} && git pull", p, b)
