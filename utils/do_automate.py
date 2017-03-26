#!/usr/bin/python3
"""
Script to automate actions on Digital Ocean droplets.
TODO:
	Urgent:
	- Know if action was successful by checking sta
	  continously.

	- Make the script create a new droplet to make
	  snapshots to enable complete automation.
	  (maybe even backup using rsync as well)
	- Send e-mail on success (status -> if 'snapshot complete' and date present)

do_action(action) -> get_id -> get_status -> when True -> do_another_action
"""
import subprocess
import json
from time import strftime, sleep
from sys import argv


TOKEN = '044305d469fb32a48b2ecca31cb089ca34a50a70f5deac0d003ce6d86bb527c6'
DROPLET = 3502760
HOSTNAME = 'OCEANIC'
PAGE = "https://api.digitalocean.com/v2/droplets/{0}/actions?{{0}}".format(DROPLET)
DATE = strftime('%d %b %Y').upper()
BASE = "curl -s -X POST -H 'Content-Type: application/json' -H 'Authorization: \
Bearer {token}' '{page}'".format(token=TOKEN, page=PAGE)


def do_action(action='', base=BASE):
	def cmd(command):
		return subprocess.check_output(command, universal_newlines=True, shell=True)

	return cmd(base.format(action))


def power_on():
	return do_action(action='type=power_on')


def do_snapshot():
	def shutdown():
		return do_action(action='type=shutdown')

	def snapshot(name):
		action = 'type=snapshot&name=' + name
		return do_action(action=action)

	print('Issuing shutdown...')
	response = shutdown()
	print(response)
	"""
	data = shutdown()
	id = get_id(data)
	while not get_status(id): # while action is not complete
		time.sleep(30)
	# action is complete when we're out of while
	"""

	# Here, again, get the ID of the shutdown action.
	# Check every once in a while to see if it's done.
	# Only then issue the snapshot action.

	# Add tests here to know when dropet has shutdown.
	"""
	print('Sleeping...')
	sleep(60)
	# -----

	print('Isusing snapshot...')
	snapshot(name='{0} - {1}'.format(HOSTNAME, DATE).replace(' ', '%20'))
	"""
	sleep(600)
	response = snapshot(name='{0} - {1}'.format(HOSTNAME, DATE).replace(' ', '%20'))
	print(response)

	# Get ID of the action by get_status(), by
	# parsing JSON.
	# Check every so often if the action has completed.
	# Send email when it has.

"""
def get_id(data):
	id = json.parse(data).get_action_id()
	return id
"""


def get_status():
	"""
	This needs to get the status of the actions applied
	to the droplet, and save the IDs for tracking.
	Then, we need to track the status of a given action by its ID.
	return True when the action (given by ID) is done.
	so something like:
	def get_status(action_id=None):
		raw_data = do_action('page=1&per_page=1', base=base)
		status = json.parse(raw_data).get_status_field_only()
		if status == 'completed':
			return True
		else:
			return False
	"""
	base = BASE.replace('POST', 'GET')
	raw_data = do_action('page=1&per_page=1', base=base)
	json_data = json.dumps(json.loads(raw_data), sort_keys=True, indent=4,
						   separators=(',', ': '))
	data = json_data.split('\n')
	# JSON parse?
	for line in data:
		print(line)


def get_help():
	helpstr = """Available actions:
	snapshot
	status
	power_on
	"""
	print(helpstr)


def main():
	try:
		arg = argv[1]
		if arg == 'snapshot':
			do_snapshot()
		elif arg == 'status':
			get_status()
		elif arg == 'power_on':
			power_on()
		elif arg == 'help':
			get_help()

	except IndexError:
		print("Please specify an action.\nTry 'help' for a list of actions.")


if __name__ == "__main__":
	main()
