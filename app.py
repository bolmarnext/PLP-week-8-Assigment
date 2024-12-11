# app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        # Fetching weather data from OpenWeatherMap
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        # If the city is not found
        if data['cod'] != 200:
            return render_template('index.html', error="City not found!")
        
        # Extracting necessary weather details
        main = data['main']
        weather = data['weather'][0]
        city_name = data['name']
        temp = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        return render_template('index.html', city=city_name, temp=temp, humidity=humidity, description=description)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)