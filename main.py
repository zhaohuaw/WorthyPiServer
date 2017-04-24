from flask import Flask
from flask import render_template
from radio import Radio

app = Flask(__name__)
myRadio = Radio()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/radio/play')
def radio_play():
    myRadio.play()
    return 'play'


@app.route('/radio/stop')
def radio_stop():
    myRadio.stop()
    return 'stop'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8800)
    #app.run()