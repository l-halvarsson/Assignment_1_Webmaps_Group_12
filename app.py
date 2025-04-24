import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Tillåt frontend att anropa API

API_KEY = 'd0db11e853f00b2dc16776f5c49ad76d'  # Din riktiga API-nyckel


# Starta sidan
@app.route('/')
def index():
    return render_template('index.html')  # Laddar din HTML-karta

# API-funktion för att hämta väder
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    current_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'

    current = requests.get(current_url).json()
    forecast = requests.get(forecast_url).json()

    return jsonify({
        "current": current,
        "forecast": forecast
    })

if __name__ == '__main__':
    app.run(debug=True) 
