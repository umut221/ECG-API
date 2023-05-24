const mongoose = require("mongoose");
require('dotenv/config');

const connectionString = process.env.connection_string;

exports.mongoConnect = () => {
  mongoose.set("strictQuery", false);
  mongoose
    .connect(connectionString)
    .then(() => {
      console.log("Connected to database.");
    })
    .catch((err) => {
      console.log(err);
    });
};
