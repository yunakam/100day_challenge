from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = '6e08078b1e62f2a8fd37233c6f1c8026'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
