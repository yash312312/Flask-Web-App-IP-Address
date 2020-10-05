import ipinfo
from flask import Flask, render_template, request, session

app = Flask(__name__)


def getloc(ip):
    access_token = '06fa123306e582'
    handler = ipinfo.getHandler(access_token)
    ip_address = ip
    try:
        details = handler.getDetails(ip_address)
        return details.all
    except:
        return {}


app.secret_key = "ipAddress"


@app.route("/", methods=['GET', 'POST'])
def home():
    city = ''
    state = ''
    d = {}
    lat = 0.0
    lon = 0.0
    if request.method == 'POST':
        session['ip'] = request.form.get('ip')
        d = getloc(session['ip'])
        if d:
            lat = d['latitude']
            lon = d['longitude']

    return render_template('index.html', ip=session['ip'] if 'ip' in session else None,
                           ifInvalid='Invalid IP' if not d else '', list=d, lat=lat, lon=lon)


if __name__ == "__main__":
    app.run(debug=True)
