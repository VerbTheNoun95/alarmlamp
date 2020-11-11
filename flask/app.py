from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

hours = [ '0' + str(i) if len(str(i)) == 1 else str(i) for i in list(range(0,24)) ]
minutes = [ '0' + str(i) if len(str(i)) == 1 else str(i) for i in list(range(0,60)) ]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("dropdown.html", hours=hours, minutes=minutes)

@app.route('/time', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        hour = request.form.get("hours", None)
        minute = request.form.get("minutes", None)
        output = {'hour': hour, 'minute': minute}
        with open('time.json', 'w') as outfile:
            json.dump(output, outfile)

        if hour != None and minute != None:
            return render_template("dropdown.html", hours=hours, minutes=minutes, hour=hour, minute=minute)

    return render_template("dropdown.html", hours=hours, minutes=minutes, hour=hour, minute=minute)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
