from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    temp = data.get("temperature")
    humidity = data.get("humidity")
    rainfall = data.get("rainfall")
    
    if rainfall > 100:
        crop = "Rice"
    else:
        crop = "Wheat"
    
    return jsonify({"recommended_crop": crop})

if __name__ == '__main__':
    app.run(debug=True)

weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=11&longitude=78&current_weather=true").json()
print(weather["current_weather"])
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=11&longitude=78&current_weather=true"
response = requests.get(url)

data = response.json()

print("Temperature:", data["current_weather"]["temperature"])
print("Wind Speed:", data["current_weather"]["windspeed"])