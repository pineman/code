from mpd import MPDClient
MPD_SOCKET = '/home/pineman/.config/mpd/socket'
client = MPDClient()
client.connect(MPD_SOCKET, 0)

def get_mpd_data():
	idle = client.idle()
	if idle[0] == 'player':
		state = client.status()['state']
		print(state)
		wanted = ['play', 'pause']
		if state in wanted:
			info = client.currentsong()
			try:
				artist = info['artist']
				title = info['title']
				value = '{0} - {1}'.format(artist, title)
			except KeyError:
				filename = info['file']
				value = filename.split('/')[-1][:-4]
			finally:
				data = {'song': value}
				return data

print(client.outputs())