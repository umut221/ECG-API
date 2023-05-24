const express = require("express");
const router = express.Router();
const patientController = require('../controllers/patientController');

router.get('/getAll', patientController.getAll);
router.post("/create", patientController.create);
router.get('/getById/:id', patientController.getById);

module.exports = router;