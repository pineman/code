#!/usr/bin/env python3
"""
Mini-CMS for pineblog
http://blog.pineman.sexy
"""

# pineblog Copyleft - All Rights Reversed (ↄ) 2015 João Pinheiro

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Extracts data and html from files to display as posts.
Credits:
	pineman <pineman@pineman.sexy>
	Diogo Tito [https://github.com/tito97]:
		for algorithm improvements on get_data()
	Rodrigo Serrão [https://github.com/RojerGS]:
		for exec(templates)
"""

import flask
import os
import time
from random import choice
from math import ceil

pineblog = flask.Flask(__name__)
pineblog.jinja_env.trim_blocks = True
pineblog.jinja_env.lstrip_blocks = True
# http://stackoverflow.com/questions/9767585/insert-static-files-literally-into-jinja-templates-without-parsing-them
pineblog.jinja_env.globals['include_raw'] = lambda filename: flask.Markup(pineblog.jinja_loader.get_source(pineblog.jinja_env, filename)[0])

# Constants
posts_per_page = 3

# Globals
data = []
number_of_pages = None


def log(message):
	with open('log', 'a') as logfile:
		epoch = str(time.time())
		microseconds = epoch.split('.')[-1]  # extra resolution for seconds
		logtime = time.strftime('[%d/%m/%Y %H:%M:%S.{0}]'.format(microseconds))
		logfile.write('{0} {1}\n'.format(logtime, message))


def get_data():
	log('Starting postloop.')
	files = os.listdir('posts')
	log('\t--> Reading post info...')
	for filename in files:
		try:
			with open(os.path.join('posts', filename), 'r') as post:
				filename = filename.replace('.html', '')
				post = tuple(post)
				excerpt = tuple(post[6:8])
				content = tuple(post[6:])
				post = [line.strip() for line in post[:5]]
				title, date, time, author, tags = post
				tags = tags.split(',')
				global data
				data.append({'filename': filename, 'title': title, 'date': date,
				             'author': author, 'time': time, 'tags': tags,
				             'content': content, 'excerpt': excerpt})
		except Exception as error:
			log('{0}: Couldnt read post: {1}'.format(error, filename))
			continue

	log('\t--> Sorting posts by date...')
	try:
		from time import strptime
		data.sort(key=lambda post: strptime(post['date'], '%d/%m/%Y'),
				  reverse=True)
	except Exception as error:
		log(error)

	log('Postloop complete.')

	# Extra bit for page control
	number_of_posts = len(files)
	global number_of_pages
	number_of_pages = ceil(number_of_posts / posts_per_page)

# ---------- Routing -------------------------------------------------------

pineblog.before_first_request(get_data)


def render(*args, **kwargs):
	def open_and_randomize(sentencesfile):
		"""
		Takes a file with sentences and returns one sentence at random.
		"""
		try:
			with open(sentencesfile, 'r') as sentences_file:
				sentences = []
				for sentence in sentences_file.readlines():
					if not sentence.startswith('#'):
						sentences.append(sentence)
				return choice(sentences)
		except Exception:
			return "I'm a terrible programmer"

	footer_sentence = flask.Markup(open_and_randomize('footer_sentences.html'))

	return flask.render_template(footer_sentence=footer_sentence,
								 *args, **kwargs)


@pineblog.route('/control', methods=['POST'])
def control():
	song = flask.request.form.get('song')
	date = flask.request.form.get('date')
	with open('static/mpd_now_playing.txt', 'w') as mpd_data:
		mpd_data.write('{0}\n{1}'.format(song, date))
	return 'Accepted.'


@pineblog.route('/')
@pineblog.route('/page/<int:requested_page>')
def page(requested_page=1):
	if requested_page <= 0 or requested_page > number_of_pages:
		flask.abort(404)
	# So now we can safely assume 0 < requested_page <= number_of_pages
	# and type(requested_page) = int

	# Post control
	first_post = (requested_page - 1) * posts_per_page
	last_post = first_post + posts_per_page
	page = data[first_post:last_post]

	# Page buttons control
	if number_of_pages > 5:
		page_before, page_after = None, None
		ellipsize_before, ellipsize_after = False, False
		last_page = number_of_pages
		is_first_page, is_last_page = False, False

		# Does the page have one before it
		if requested_page not in [1, 2]:
			page_before = requested_page - 1
			if page_before != 2:
				ellipsize_before = True
		# If not its either the second or the first one
		elif requested_page == 1:
			is_first_page = True

		# Does the page have one after it
		penultimate_page = last_page - 1
		if requested_page not in [penultimate_page, last_page]:
			page_after = requested_page + 1
			if page_after != penultimate_page:
				ellipsize_after = True
		# If not its either the penultimate or the last one
		elif requested_page == last_page:
			is_last_page = True

		# u better be ready son
		return render('page.html', data=page,
					  last_page=last_page,
					  is_first_page=is_first_page,
					  is_last_page=is_last_page,
					  ellipsize_before=ellipsize_before,
					  ellipsize_after=ellipsize_after,
					  requested_page=requested_page,
					  page_before=page_before,
					  page_after=page_after)
	else:
		return render('page.html', data=page,
					  number_of_pages=number_of_pages)


@pineblog.route('/posts/<post>')
def post(post):
	# Check if post exists by the filename
	# for...else madness
	for posts in data:
		if post == posts['filename']:
			return render('post.html', post=posts)
	else:
		flask.abort(404)


@pineblog.route('/tagged/<tag>')
def tags(tag):
	# Retrieve posts whose tags match the requested tag
	tagsdata = [postdata for postdata in data if tag in postdata['tags']]
	# If any exist, return, else, abort with a 404
	if tagsdata:
		return render('tags.html', data=tagsdata, tag=tag)
	else:
		flask.abort(404)


@pineblog.route('/about')
def about():
	with open('static/mpd_now_playing.txt', 'r') as mpd_data_file:
		mpd_data = [line.strip() for line in mpd_data_file]
	return render('pages/about.html',
				  mpd_data=mpd_data)


## contributed by Rodrigo Serrão [https://github.com/RojerGS] with modifications
#pages = os.listdir('templates/pages')
#
#template = """\
#@pineblog.route('/{0}')
#def {0}():
#	return render('pages/{0}.html')
#"""
#
#for page in pages:
#	page = page.replace('.html', '')
#	exec(template.format(page))
## --------------------------

import atexit
atexit.register(log, 'Exited.')

if __name__ == '__main__':
	pineblog.run(debug=True, host='0.0.0.0', port=8080)
