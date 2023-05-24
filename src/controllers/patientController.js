const patientService = require('../services/patientService');


exports.getAll = async (req, res) => {
    const result = await patientService.getAll();
    res.send(result);
}

exports.create = async ( req, res) => {
    const result = await patientService.create(req.body);
    res.send(result);
}

exports.getById = async(req,res) => {
    return null;
}