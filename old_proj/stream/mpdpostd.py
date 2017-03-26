#!/usr/bin/env python3

from mpd import MPDClient
from requests import post
#from secrets import secrets # Get personal passwords
# NOTE: the 'secrets' module didn't exist at the time
from time import sleep, strftime

POST_URL = 'http://blog.pineman.sexy/control'
MPD_SOCKET = '/home/pineman/.config/mpd/socket'
client = MPDClient()
client.connect(MPD_SOCKET, '')
data = {'song': ''}

def get_mpd_data():
	idle = client.idle()
	if idle[0] == 'player':
		state = client.status()['state']
		wanted = ['play']
		if state in wanted:
			info = client.currentsong()
			try:
				artist = info['artist']
				title = info['title']
				song = '{0} - {1}'.format(artist, title)
			except KeyError:
				filename = info['file']
				song = filename.split('/')[-1][:-4]
			finally:
				global data
				if data['song'] != song:
					data = {'date': strftime('%X %Z %a, %d %b'), 'song': song}
					return data
				else:
					return None
		else:
			return None


def post_mpd_data(data):
	"""POST the data as post data, not url-encoded params"""
	try:
		print(data)
		user = secrets[0]
		password = secrets[1]
		request = post(POST_URL, data=data, auth=(user, password))
		print('success')
	except Exception as error:
		print('error:\n{0}'.format(error))


def main():
	while True:
		data = get_mpd_data()
		if data:
			post_mpd_data(data)


if __name__ == '__main__':
	main()
