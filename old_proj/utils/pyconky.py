"""
Script to manage Conky.
Give conky the necessary information (by printing it)
for a field specified using command line arguments.
"""

from subprocess import getoutput, call
from shutil import copy2
from sys import argv, exit
from socket import gethostbyname
import os


COLOR1 = "${color1}"
COLOR2 = "${color2}"
COLOR3 = "${color3}"
END = "$color"


def check_updates():
	updates = getoutput('checkupdates').split()
	number_of_updates = len(updates)

	if number_of_updates == 0:
		print("{0}No updates available.{1}".format(COLOR1, END))
	elif number_of_updates == 1:
		print("{0}1 Update available.{1}".format(COLOR1, END))
	else:
		print("{0}{1} Updates available.{2}".format(COLOR1, number_of_updates, END))


def music(external=True):
	mpc = 'mpc -h /home/pineman/.config/mpd/socket --format'

	def mpc_parser(data):
		command = '{0} %{1}%'.format(mpc, data)
		result = getoutput(command)
		result = result.split('\n')[0]
		return result

	def album_art(song):
		art_path = os.path.join('/home/pineman/Music/', song)
		cover_path = os.path.join(art_path, 'cover.jpg')
		if os.path.isfile(cover_path):
			return cover_path
		else:
			return False

	track = mpc_parser('track')
	album = mpc_parser('album')

	if not track:
		relative_path = mpc_parser('file').split('/')[-1]
		print("  " + relative_path[:-4])
		print("  $mpd_elapsed / $mpd_length")
		if album:
						print("  " + album)
	else:
		date = mpc_parser('date')
		title = mpc_parser('title')
		artist = mpc_parser('artist')
		print("  {0}. {1}  ($mpd_elapsed / $mpd_length)".format(track, title))
		print("  {0}".format(artist))
		print("  {0}  [{1}]".format(album, date))

	base_path = mpc_parser('file')
	base_path = os.path.split(base_path)[0]
	cover = album_art(base_path)

	if cover:
		copy2(cover, '/tmp/')
		if check_battery():
			print('${image /tmp/cover.jpg -p 7,870 -s 150x150 -n}')
		else:
			if external:
				print('${image /tmp/cover.jpg -p 9,535 -s 150x150 -n}')
			else:
				print('${image /tmp/cover.jpg -p 9,533 -s 150x150 -n}')

		for i in range(5):
			print(' ')


def check_battery():
	battery_status = getoutput('acpi')
	if '100' in battery_status:
		return False
		#return True
	else:
		return False

def print_battery():
	if check_battery():
		print('\n${color1}Time Left:$color $battery_time')


def network_iface_ip():
	iface_tmp = getoutput('nmcli -t --fields DEVICE connection show --active')
	iface = iface_tmp.split()[0]
	print(iface)

	with open('/tmp/iface', 'w') as ifacefile:
		ifacefile.write(iface)

		#ip_address = getoutput('curl icanhazip.com 2>/dev/null')
		ip_address = getoutput("ip -4 -o addr show scope global | awk '{print $4}'")

	print('  ${{color1}}IP Address:$color {0}'.format(ip_address))


def network_up_down():
	with open('/tmp/iface', 'r') as ifacefile:
		iface = ifacefile.readlines()[0]
	print('  •	${color1}Up:$color ${upspeed ' + iface + '}')
	print('  •	${color1}Down:$color ${downspeed ' + iface + '}')


def main():
	arg = argv[1]

	if arg == 'updates':
		check_updates()
	elif arg == 'battery':
		print_battery()
	elif arg == 'network_iface':
		network_iface_ip()
	elif arg == 'network_speed':
		network_up_down()
	elif arg == 'music':
		music()
	elif arg == 'music-lap':
		music(external=False)

	exit(0)


if __name__ == "__main__":
	main()
