const fetch = require('node-fetch')
let input = await fetch('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-gullbursdag.txt')
.then(line=>line.text())
.then(line=>line.split('\n'))

console.log(input)