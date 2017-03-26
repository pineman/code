#!/usr/bin/env python3

import sys
import subprocess
import time


while True:
	time.sleep(10)
	cmd = subprocess.check_output('ssh hackmobile acpi', shell=True, universal_newlines=True)

	if '100' in cmd:
		subprocess.call("notify-send -i battery 'Hackmobile' 'Battery done charging'", shell=True)
		break
