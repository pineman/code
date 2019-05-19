# soundboard webapp
soundboard
supports user uploads

## roadmap:
- tech:
	- node.js for backend
		- sqlite for db
		- mustache for templates
	- LESS for css [bootstrap?]
	- something to build production website (minify JS [closure compiler], html & templates, gzip)

- nginx serves static files and pages:

- else proxy to node.js (nginx reverse proxy cache)
	- implement etags and 304s
	- RESTful api
	- render templates for frontpage and user soundboards
	- pages: 
		- / [high cache]
			- header, highest-rated buttons, login form [set session cookie client & server db]
		- /myboard [low cache]
			- query users buttons if session valid else go to /login
			- users can add public buttons (update db but show new instantaneously)
			- take care with cache policy ["private no-cache" ?]

- learn:
	- users
	- sql
	- better JS (node)
	- nginx reverse proxy cache
