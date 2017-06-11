from flask import Flask, render_template, request, jsonify
import gpio_server as servo
import os, signal, subprocess, time, atexit

app = Flask(__name__)

cmd = "/home/pi/eslab/streaming.sh"
path = "/home/pi/mjpg-streamer/mjpg-streamer-experimental/"
proc = None

motor = servo.ServoController(18)
motor.setDutyCycle(6)
step = 1

#####################
#      SERVER       #
#####################

def kill_child():
    global proc
    if proc is None:
        pass
    else:
	child_pid = proc.pid
        if child_pid is None:
            pass
	else:
       	    os.killpg(os.getpgid(child_pid), signal.SIGTERM)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/streaming', methods=['PUT'])
def stream():
    global cmd, path, proc
    
    if request.json['command'] == '1':
        print 'ON'
        proc = subprocess.Popen(cmd, shell=True, cwd=path, preexec_fn=os.setsid)
        res = {'test': 'streaming on'}
        return jsonify(res)
    else:
        print 'OFF'
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        res = {'test': 'streaming off'}
        return jsonify(res)

@app.route('/api/capture', methods=['PUT'])
def capture():
    currTime = time.localtime()
    timeString = ""
    for i in range(0, 5):
        timeString = timeString + str(currTime[i]) + "_"
    i = 5
    timeString = timeString + str(currTime[i])
        
    if request.json['command'] == '1':
        print 'CAPTURING'
        subprocess.Popen(['wget', 'http://localhost:9090/?action=snapshot', '-O', 'output' + timeString + '.jpg'])
        res = {'test': 'captured'}
        return jsonify(res)

@app.route('/api/rotate', methods=['PUT'])
def rotate():

    global angle, step
    
    if request.json['command'] == '1':
        print 'UP'

        motor.incDutyCycle(step)

        res = {'test': 'up'}
        return jsonify(res)
    else:
        print 'DOWN'

        motor.incDutyCycle(-step)
        
        res = {'test': 'down'}
        return jsonify(res)


if __name__ == '__main__':

    atexit.register(kill_child)

    app.run(
        host='192.168.0.1',
        port=int("5000"),
        debug=True
    )

