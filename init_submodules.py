#!/usr/bin/env python3

from configparser import ConfigParser
from subprocess import call
from shlex import quote


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
