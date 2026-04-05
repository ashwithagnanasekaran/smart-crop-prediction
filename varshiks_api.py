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
weather = get_weather()
temp = weather["temperature"]
if temp > 30 and humidity > 60:
    crop = "Rice"
elif rainfall < 50:
    crop = "Millet"
    # calculate simple weather score
score = temp + humidity + rainfall
print("Weather Score:", score)
# status check
status = "prediction success"
print(status)
# handle API error
if response.status_code != 200:
    print("API request failed")
    return {
    "temperature": data["current_weather"]["temperature"],
    "windspeed": data["current_weather"]["windspeed"]
}
# fetch current weather data from open-meteo API
response = requests.get(url, timeout=5)