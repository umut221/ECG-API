const mongoose = require("mongoose");
const patientSchema = mongoose.Schema({

    name: {
        type: String,
        required: true
    },
    age: {
        type: Number,
        required: true
    },
    gender: {
        type: String,
        enum: ['Erkek', 'Kadın'],
        default: 'Erkek'
    },

    ecgValues: mongoose.Schema.Types.Mixed,

    createdDate:{
        type: Date,
        default: Date.now
    }
});

exports.Patient = mongoose.model("Patient", patientSchema);