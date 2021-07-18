#!/usr/bin/env python3

from configparser import ConfigParser
from subprocess import call


def sh(cmd):
    try:
        r = call(f"cd {p} && git checkout {b} && git pull", shell=True)
        if r != 0:
            __import__("sys").exit(r)
    except Exception as e:
        print(e)


sh("git submodule update --init --recursive")
c = ConfigParser()
c.read(".gitmodules")
for s in c.sections():
    p = c[s]["path"]
    try:
        b = c[s]["branch"]
    except:
        continue
    sh(f"echo {p}; cd {p} && git checkout {b} && git pull")
