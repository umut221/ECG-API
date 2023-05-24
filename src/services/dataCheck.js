const mailService = require("./mailService");

exports.getData = async () => {
    const data = getDataFromAPI();
    return data;
};

exports.getAnalyze = async (patient = "İsimsiz Hasta") => {
    const data = getDataFromAPI();
    const analyze = getAnalyzeFromAPI();
    if(analyze.bpm>140 || analyze.bpm<40){
        mailService.sendMail("doktorMaili@gmail.com", "Tehlikeli Durum", `<h1>${patient} Isimli Hastanın Kritik Durumdaki Bilgileri</h1><br><p>Analiz edilmiş veri: ${analyze}</p><br><p>Ham veri: ${data}`);
        return analyze;
    }else{
        return analyze;
    }
}

async function getDataFromAPI() {
    const response = await fetch("http://127.0.0.1:5000");
    const json = await response.json();
    return json;
  }

async function getAnalyzeFromAPI() {
    const response = await fetch("http://127.0.0.1:5000/analyze");
    const textData = await response.text();
    return textData;
  }
