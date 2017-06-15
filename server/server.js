'use strict'

const restify = require('restify');
const request = require('request');
const path = require('path');
const fs = require('fs');
const server = restify.createServer();
let ipList = {};
let database = {};
// let database = { "a": { coordN: 25.0157539, coordE: 121.5415932 }, "b": { coordN: 25.0563711, coordE: 121.5155881 }, "c": { coordN: 25.0431791, coordE: 121.5511676 } };


const dataDir = './data/'

function readJSON(file) {
    let obj = null;
    fs.readFile(dataDir + file, 'utf8', function (err, data) {
        if (err) throw err;
        obj = JSON.parse(data);

        let name = obj['file_name'];
        name = name.substr(0, name.length - 4);
        let lat = parseFloat(obj['lat']);
        let lng = parseFloat(obj['lng']);

        database[name] = {'coordE': lat, 'coordN': lng}

    });
}

fs.readdir(dataDir, function(err, files) {
    files.forEach(readJSON);
});

server.use(restify.bodyParser());
server.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});
server.listen(3333, () => {
  console.log('%s listening to %s', server.name, server.url);
});

server.get('/api/cases', (req, res) => {
  let body = {
    timestamp: Date.now(),
    data: [],
  };
  for (let key in database) {
    if (database.hasOwnProperty(key)) {
      let deviceData = database[key];
      deviceData.caseId = key;
      body.data.push(deviceData);
    }
  }
  console.log(body);
  res.send(200, JSON.stringify(body));
});

server.post('/api/case', (req, res) => {
  const id = req.body.caseId;
  try {
    if (!database.hasOwnProperty(id)) {
      throw Error('bad request');
    }
  } catch (err) {
    console.error(err);
    res.send(400);
  }

  const body = {
    deviceId: id,
    timestamp: Date.now(),
  };

  res.send(200, JSON.stringify(body));
});

server.post('/api/report', (req, res) => {
  let body = req.body;
  if (body.length !== undefined) {
    for (let i = 0; i < body.length; i += 1) {
      database[body[i].name] = { coordE: body[i].lng, coordN: body[i].lat };
    }
  } else {
    database[body.name] = { coordE: body.lng, coordN: body.lat };
  }
  res.sendStatus(202);
});

server.get(/\/*/, restify.serveStatic({
  directory: path.join(__dirname, '/public'),
  default: 'index.html',
}));
