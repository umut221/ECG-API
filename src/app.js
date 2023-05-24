const express = require("express");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const cors = require("cors");
const mongo = require("./db/mongoConfig");
const errorHandler = require("./helpers/error-handler");

const dataCheck = require('./services/dataCheck');

const app = express();
const http = require("http").createServer(app);
const io = require("socket.io")(http, {
  cors: {
    origins: ["http://localhost:4200"],
  },
});

const patientRouter = require("./routers/patientRouter");

require("dotenv/config");
const port = process.env.PORT;
const api = process.env.API_URL;

app.use(cors());
app.options("*", cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(morgan("tiny"));
app.use(errorHandler);

app.use("/patients", patientRouter);

io.on("connection", (socket) => {
  console.log("Client connected");
  dataUpdate(socket);
  analyzeData(socket);
});

async function dataUpdate(socket) {
  socket.emit("dataUpdate", await dataCheck.getData());
  setTimeout(() => {
    dataUpdate(socket);
  }, 2500);
}

async function analyzeData(socket){
  socket.emit('analyzeData', await dataCheck.getAnalyze());
  setTimeout(() => {
    analyzeData(socket);
  }, 2500);
}

http.listen(port, async () => {
  mongo.mongoConnect();
  console.log(`port: ${port} is listening for ${api}`);
});


module.exports = app;
