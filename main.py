from flask import Flask
from flask import render_template
import os
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/radio/play')
def radio_play():
    subprocess.call('mplayer http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws')
    print('radio play')

@app.route('/radio/stop')
def radio_stop():
    subprocess.call('mplayer q')
    print('radio stop')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
    #app.run()