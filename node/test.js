var path = require("path");
var hello = "Hello from JS Variable"
console.log('Printing variable hello: ${hello}');
console.log("Directory name = " + __dirname);
console.log("directory and file name = " + __filename);
console.log("using PATH module:");
console.log('hello from file ' + path.basename(__filename));
console.log("Process.args: "+ process.argv)