const cluster = require('cluster');
const http = require('http');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
	console.log(`Master ${process.pid} is running`);
	// Fork workers.
	for (let i = 0; i < numCPUs; i++) {
		cluster.fork();
	}
	cluster.on('exit', (worker, code, signal) => {
		console.log(`Worker ${worker.process.pid} died`);
	});
} else {
	console.log(`Worker ${process.pid} started`);
	// Workers can share any TCP connection
	// In this case it is an HTTP server
	http.createServer((req, res) => {
		res.writeHead(200);
		res.end(`hello from worker ${process.pid}\n`);
		console.log(`Worker ${process.pid} served request`);
	}).listen(8000);
}
