import random
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import heartpy as hp
import numpy as np
import math

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

data = []

# datas, _ = hp.load_exampledata(2)
# enchanced = hp.enhance_peaks(datas,iterations=2)
# working_data, measures = hp.process(datas, 100.0, report_time=True)
# enhanced = hp.enhance_peaks(datas, iterations=2)


@app.route('/')
@cross_origin()
def sendData():
  
  return jsonify(generate_ekg_data())

@app.route('/analyze')
def sendAnalyze():
  
  return make_response(jsonify(analyzeData()))

def generate_ekg_data():

    
    #requests        data = requests.get('https://ekgverisiBurada.com/data?hastaId=123123123123123');

    ekg_data = []
    total_waves = 5
    samples_per_wave = 7500 // total_waves

    for wave in range(total_waves):
        # P dalgası
        p_duration = random.randint(samples_per_wave // 20, samples_per_wave // 10)
        for i in range(p_duration):
            t = i / samples_per_wave
            value = 0.15 * math.sin(2 * math.pi * 6 * t) * (1 + random.uniform(-0.05, 0.05))
            ekg_data.append(value)

        # Q dalgası
        q_duration = random.randint(samples_per_wave // 50, samples_per_wave // 25)
        for i in range(q_duration):
            t = i / samples_per_wave
            value = -0.25 * math.sin(2 * math.pi * 12 * t) * (1 + random.uniform(-0.05, 0.05))
            ekg_data.append(value)

        # R dalgası
        r_duration = random.randint(samples_per_wave // 15, samples_per_wave // 7)    # 20------10
        for i in range(r_duration):
            t = i / samples_per_wave
            value = 1.2 * math.sin(2 * math.pi * 6 * t) * (1 + random.uniform(-0.05, 0.05))
            ekg_data.append(value)

        # S dalgası
        s_duration = random.randint(samples_per_wave // 50, samples_per_wave // 25)
        for i in range(s_duration):
            t = i / samples_per_wave
            value = -0.75 * math.sin(2 * math.pi * 12 * t) * (1 + random.uniform(-0.05, 0.05))
            ekg_data.append(value)

        # T dalgası
        t_duration = random.randint(samples_per_wave // 10, samples_per_wave // 5)
        for i in range(t_duration):
            t = i / samples_per_wave
            value = 0.4 * math.sin(2 * math.pi * 4 * t) * (1 + random.uniform(-0.05, 0.05))
            ekg_data.append(value)

        # İzoelektrik çizgi
        iso_duration = samples_per_wave - p_duration - q_duration - r_duration - s_duration - t_duration - random.randint(15,25)
        for i in range(iso_duration):
            ekg_data.append(0)

    return ekg_data

def igenerate_ekg_data():
    
    fs = 1000  # örnekleme frekansı
    duration = 1  # sinyal süresi
    samples = int(fs * duration)  # toplam örnek sayısı
    t = [float(i) / fs for i in range(samples)]  # zaman dizisi
    ecg_data = []

    # EKG verisi için dalga parametrelerinin tanımlanması
    p_amp = random.uniform(0.1, 0.3)
    p_dur = random.uniform(0.1, 0.2)
    p_phase = random.uniform(0, math.pi)
    q_amp = random.uniform(-0.1, 0.1)
    q_dur = random.uniform(0.01, 0.03)
    q_phase = random.uniform(0, math.pi)
    r_amp = random.uniform(0.5, 1)
    r_dur = random.uniform(0.05, 0.1)
    r_phase = random.uniform(0, math.pi)
    s_amp = random.uniform(-0.2, 0)
    s_dur = random.uniform(0.05, 0.1)
    s_phase = random.uniform(0, math.pi)
    t_amp = random.uniform(0.2, 0.4)
    t_dur = random.uniform(0.1, 0.2)
    t_phase = random.uniform(0, math.pi)

    # EKG verisi için sinus dalgalarının oluşturulması
    p_wave = [p_amp * math.sin(2 * math.pi * (1 / p_dur) * (i - p_phase)) for i in t]
    q_wave = [q_amp * math.sin(2 * math.pi * (1 / q_dur) * (i - q_phase)) for i in t]
    r_wave = [r_amp * math.sin(2 * math.pi * (1 / r_dur) * (i - r_phase)) for i in t]
    s_wave = [s_amp * math.sin(2 * math.pi * (1 / s_dur) * (i - s_phase)) for i in t]
    t_wave = [t_amp * math.sin(2 * math.pi * (1 / t_dur) * (i - t_phase)) for i in t]

    # EKG verisi oluşturma
    ecg = [p_wave[i] + q_wave[i] + r_wave[i] + s_wave[i] + t_wave[i] for i in range(samples)]

    # EKG verisini diziye ekleme
    ecg_data.append(ecg)
    return ecg_data[-1]


def analyzeData():
  measures = []
  processData = igenerate_ekg_data()
  working_data, measures = hp.process(processData, 100.0, report_time=True)
  return measures


if __name__ == '__main__':
    app.run(debug=True)







