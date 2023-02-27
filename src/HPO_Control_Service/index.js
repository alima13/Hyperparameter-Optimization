const express = require("express");
const mongoose = require("mongoose");
const routes = require("./routes");
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'user-service' },
  transports: [
    //
    // - Write all logs with importance level of `error` or less to `error.log`
    // - Write all logs with importance level of `info` or less to `combined.log`
    //
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});

//
// If we're not in production then log to the `console` with the format:
// `${info.level}: ${info.message} JSON.stringify({ ...rest }) `
//
if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple(),
  }));
}

mongoose
  .connect("mongodb://127.0.0.1/HPOdb?socketTimeoutMS=90000", { useNewUrlParser: true })
  .then(() => {
    const app = express();
    app.use(express.json());
    app.use("/api/v1", routes);

    app.listen(3000, () => {
      console.log("*** HPO_Optimization_Engine:V1.1 ***","\n","Status : Started Listening on port 3000");
    });
  });
