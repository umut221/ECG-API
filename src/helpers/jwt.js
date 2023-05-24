const { expressjwt: expressJwt, done: done } = require("express-jwt");

function authJwt() {
  const secret = process.env.SECRET_STRING;
  const api = process.env.API_URL;
  return expressJwt({
    secret,
    algorithms: ["HS256"],
    isRevoked: isRevoked,
  }).unless({
    path: [
      { url: /\/api\/v1\/products(.*)/, methods: ["GET", "OPTIONS"] },
      { url: /\/api\/v1\/categories(.*)/, methods: ["GET", "OPTIONS"] },
      `${api}/auth/login`,
      `${api}/auth/register`,
      /\/api\/v1\/auth\/confirm\/(.*)/,
    ],
  });
}

async function isRevoked(req, payload) {
  if (!payload.payload.isAdmin) return true;
  return undefined;

}

module.exports = authJwt;
