from flask import Flask, render_template, request
from weather import get_current_weather
import os
# from waitress import serve



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    # return render_template('index.html')
    if request.method == "POST":

        if request.form:
            return 'Form submited'
    else:
        return render_template('index.html')
    



@app.route('/weather', methods=["GET", "POST"])
def get_weather():

    if request.method == "GET":
        city = request.args.get('city')
    elif request.method == 'POST':
        city = request.form['city']

    if not city.strip():
        city = 'Osogbo'

    weather_data = get_current_weather(city)

    if not weather_data['cod'] == 200:
        return render_template('error page.html',
                               message = weather_data['message'].title())
    
    return render_template('weather.html', 
                           title = weather_data['name'],
                           status = weather_data['weather'][0]['description'].capitalize(),
                           feels_like = weather_data['main']['feels_like'],
                           temp = weather_data['main']['temp']
                           )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=port, debug=True)
    # serve(app, host='0.0.0.0', port=8000)
    