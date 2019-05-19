import logging as log
import sys
import magic
import sqlite3
import pystache

# Constants
REQUIRED_FIELDS = set(('audio', 'name'))
AUDIO_MIMETYPES = ('audio/mpeg', 'audio/ogg')
AUDIO_FILE_EXTS = ('.mp3', '.ogg')
MAX_NAME_SIZE = 30
HTTP_STATUS = {400: '400 Bad Request',
			   415: '415 Unsupported Media Type',
			   200: '200 OK',
			   201: '201 Created',
			   405: '405 Method Not Allowed',
			   421: '421 Misdirected Request'}


# Generic object to hold necessary response attributes
class Response:
	def __init__(self):
		self.headers = [('Content-Length', '0')]
		self.status = ''
		self.response = ''.encode('utf-8')


log.basicConfig(level=log.DEBUG,
				stream=sys.stdout,
				style='{', format='[{asctime} {levelname}] {message}')


def upload(env, resp):
	success = False
	resp.headers = [('Content-Type', 'text/html; charset=utf-8')]

	# Search for required fields
	if set(REQUIRED_FIELDS) != set(form.keys()):
		resp.status = HTTP_STATUS[400]
		resp.response = 'Please fill all the required form fields.'

	# Check for max length
	elif len(str(form['name'].value)) > MAX_NAME_SIZE:
		resp.status = HTTP_STATUS[400]
		resp.response = 'Name is too big.'

	# Check for already existing name
	#elif sql shenanigans
	#	resp.status = HTTP_STATUS[400]
	#	resp.response = 'Name already exists.'

	# Check for correct audio file mimetype
	elif (magic.from_buffer(form['audio'].file.read(), mime=True)
		  not in AUDIO_MIMETYPES):
		resp.status = HTTP_STATUS[415]
		resp.response = 'Please upload an audio file of types: ' +
						', '.join(AUDIO_FILE_EXTS)

	else:
		resp.headers.append([('Location', '/index.html')])
		resp.status = HTTP_STATUS[201]
		resp.response = 'Success! New button is live at https://sb.pineman.win'.encode('utf-8') # replace by const?
		resp.headers.append(('Content-Length', str(len(resp.response))))
		# Now save the audio file, update the DB, generate the template and gzip it
		# don't forget to validate the filename from 'name'

	return resp


def application(env, start_response):
	resp = Response()

	if env['PATH_INFO'] == '/api/v1/buttons':
		if env['REQUEST_METHOD'] != 'POST':
			resp.status = HTTP_STATUS[405]
		else:
			resp = upload(env, resp)
	else:
		log.debug('got unmanaged PATH_INFO ({})'.format(env['PATH_INFO']))
		resp.status = HTTP_STATUS[421]

	start_response(resp.status, resp.headers)
	return [resp.response]
