var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");
var math = require("math");

http.createServer(function(req, res){
	if (req.url === "/"){
		fs.readFile("./public/index.html", "UTF-8", function(err, body){
			res.writeHead(200, {"Content-Type": "text/html"});
			res.end(body);
		});
	} else if(req.url.match("/sysinfo")){
		var uptimetot = os.uptime()
		var uptimeday = math.floor(uptimetot/86400)
		var uptimehr = math.floor((uptimetot-(uptimeday*86400))/3600)
		var uptimemin = math.floor((uptimetot-((uptimeday*86400)+(uptimehr*3600)))/60)
		var uptimesec = uptimetot-((uptimeday*86400)+(uptimehr*3600)+(uptimemin*60))
		var totmem = os.totalmem()/1000000
		var fremem = os.freemem()/1000000

		myHostName = os.hostname();
		html = `
		<!DOCTYPE html>
		<html>
			<head>
				<title>Node JS Response</title>
			</head>
			<body>
				<p>Hostname: ${myHostName}</p>
				<p>IP: ${ip.address()}</p>
				<p>Server Uptime: ${uptimeday}:${uptimehr}:${uptimemin}:${uptimesec}</p>
				<p>Total Memory: ${totmem} MB</p>
				<p>Free Memory: ${fremem} MB</p>
				<p>Number of CPUs: ${os.cpus().length}</p>
			</body>
		</html>`
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(html);
	} else {
		res.writeHead(404, {"Content-Type":"text/html"});
		res.end(`404 file not found at ${req.url}`);
	}
}).listen(3000);
console.log("Server listening on port 3000");