"""
Little script to do some file renaming and things.
WHY IS EVERYTHING SO CONVOLUTED
"""

import os
import shutil
import subprocess


WAVPATH = '/run/media/pineman/Pack Rat/Music'

def movewavs():
	for root, dirs, files in os.walk(WAVPATH):
		for file in files:
			if file.endswith('wav'):
				source = os.path.join(root, file)
				destination = os.path.join(root, 'WAV', file)
				print('move {0} to {1}'.format(source, destination))
				try:
					os.rename(source, destination)
				except FileNotFoundError:
					os.mkdir(os.path.dirname(destination))
					os.rename(source, destination)


def renamewavs():
	for root, dirs, files in os.walk(WAVPATH):
		if 'WAV' in dirs:
			mp3names = [name for name in os.listdir(root) if name.endswith('mp3') and name[0:2].isdigit()]
			mp3names.sort(key=lambda name: int(name[0:2]))

			wavs = [os.path.join(root, 'WAV', wav) for wav in os.listdir(os.path.join(root, 'WAV'))]
			print(wavs)
			mp3names = mp3names[0:len(wavs)]
			print(mp3names)

			if mp3names:
				for index, wav in enumerate(wavs):
					os.rename(wav, os.path.join(root, 'WAV', mp3names[index].replace('mp3', 'wav')))

			try:
				shutil.copyfile(os.path.join(root, 'cover.jpg'), os.path.join(root, 'WAV', 'cover.jpg'))
			except FileNotFoundError:
				continue


def convertwavs():
	for root, dirs, files in os.walk(WAVPATH):
		for file in files:
			if file.endswith('wav'):
				file = os.path.join(root, file)
				print(file)
				#os.system('ffmpeg -i {0} -b:a 320k {1}'.format(file, file.replace('.wav', '.mp3')))
				subprocess.call(['ffmpeg', '-i', file, '-b:a', '320k', file.replace('wav', 'mp3')])


def main():
	#movewavs()
	#renamewavs()
	convertwavs()


if __name__ == '__main__':
	main()
