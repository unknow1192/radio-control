from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

stations = {"Nowy swiat": "https://stream.open.fm/368?type=.aac&user=800043471858&player_group=WWW"}

current_process = None
current_station = None

@app.route('/')
def index():
    return render_template('index.html', stations=stations, current_station=current_station)

@app.route('/play', methods=['POST'])
def play():
    global current_process, current_station

    station = request.form.get('station')
    url = stations.get(station)

    if current_process:
        current_process.terminate()

    current_process = subprocess.Popen(['cvlc', '--no-video', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    current_station = station

    return render_template('index.html', stations=stations, current_station=current_station)

@app.route('/stop', methods=['POST'])
def stop():
    global current_process, current_station

    if current_process:
        current_process.terminate()
        current_process = None
        current_station = None

    return render_template('index.html', stations=stations, current_station=current_station)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
