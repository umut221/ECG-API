const {Patient} = require('../models/patient');

async function getAll() {
    const patients = await Patient.find();
    return {success: true, patients: patients};
}

async function create(patient) {
    let createdPatient = new Patient({
        name: patient.name,
        age: patient.age,
        gender: patient.gender,
        ecgValues: patient.ecgValues[0]
    });
    createdPatient = await createdPatient.save();
    if(!createdPatient) return {success: false, message: "Beklenmeyen bir hata oluştu."};
    return {success: true, message: "Hasta başarıyla oluşturuldu."}
}


module.exports = {
    getAll,
    create
}