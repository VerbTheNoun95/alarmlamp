from flask import Flask, render_template, request, url_for, redirect
from apscheduler.schedulers.background import BackgroundScheduler
import json
import os
import time
from time import sleep
from datetime import datetime

from alarm_sequence import sequence, off


off()
app = Flask(__name__)

hours = [ '0' + str(i) if len(str(i)) == 1 else str(i) for i in list(range(0,24)) ]
minutes = [ '0' + str(i) if len(str(i)) == 1 else str(i) for i in list(range(0,60)) ]

sched = BackgroundScheduler(daemon=True)
sched.start()

def get_date(hour=None, minute=None):
    print(int(hour), int(minute))
    year = datetime.date(datetime.now()).year
    month = datetime.date(datetime.now()).month
    day = datetime.date(datetime.now()).day
    print(datetime.now().hour)
    print(datetime.now().minute)
    print(day)

    if int(hour) == datetime.now().hour and int(minute) <= datetime.now().minute:
        day += 1
        print(day)
    elif int(hour) < datetime.now().hour:
        day += 1
        print(day)

    return("{}-{}-{}".format(year, month, day))

if os.path.exists("time.json"):
    with open('time.json', 'r') as time_file:
        line = time_file.readline()
        time = json.loads(line)

    hour = time['hour']
    minute = time['minute']

    start_date = "{} {}:{}:00".format(get_date(hour, minute), hour, minute)
    print(start_date)
    #sched.add_job(sequence, trigger='interval', days=1, id='alarm', start_date=start_date)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("dropdown.html", hours=hours, minutes=minutes)

@app.route('/time', methods=['GET', 'POST'])
def time():

    if request.method == "POST":
        hour = request.form.get("hours", None)
        minute = request.form.get("minutes", None)
        output = {'hour': hour, 'minute': minute}
        with open('time.json', 'w') as outfile:
            json.dump(output, outfile)

        if hour != None and minute != None:
            sched.remove_all_jobs()

            start_date = "{} {}:{}:00".format(get_date(hour, minute), hour, minute)
            print(start_date)
            sched.add_job(sequence, trigger='interval', days=1, id='alarm', start_date=start_date)

            return render_template("dropdown.html", hours=hours, minutes=minutes, hour=hour, minute=minute)

    return render_template("dropdown.html", hours=hours, minutes=minutes, hour=hour, minute=minute)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
