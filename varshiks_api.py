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
data = response.json() if response.status_code == 200 else {}
temperature = data.get("current_weather", {}).get("temperature", 0)
windspeed = data.get("current_weather", {}).get("windspeed", 0)
def get_weather(lat=11, lon=78):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    """
Fetch current weather data using Open-Meteo API
Returns temperature and windspeed
"""
try:
    response = requests.get(url, timeout=5)
except Exception as e:
    print("Error fetching weather:", e)
    return {}
if "current_weather" not in data:
    print("Weather data not available")
    # create params
params = {"latitude": 13.08, "longitude": 80.27}
# add current weather flag
params["current_weather"] = True

response = requests.get(url, params=params)
weather_data = data.get("current_weather", {})
temperature = weather_data.get("temperature", 0)
wind_speed = weather_data.get("windspeed", 0)
features = [temperature, wind_speed]
print("Predicted Crop:", prediction)
if response.status_code == 200:
else:
    data = {}
temperature = weather_data.get("temperature", 25)
features = [round(temperature, 2), wind_speed]
crop_name = le_crop.inverse_transform(prediction)[0]
print("API Response:", data)
if not weather_data:
    print("No weather data available")
weather_code = weather_data.get("weathercode", 0)
rainfall = 0 if weather_code == 0 else 50
input_data = [features]
confidence = max(p
print("Confidence:", confidence)
result = f"{crop_name} ({round(confidence*100,2)}%)"
print(result)
response = requests.get(url, params=params, timeout=5)
try:
    response = requests.get(url, params=params, timeout=5)
data = response.json() if response.status_code == 200 else {}
weather_data = data.get("current_weather") or {}
temperature = round(temperature, 2)
humidity = int(humidity)
soil_type = 1
if features:
    prediction = model.predict([features])
print(f"Crop: {crop_name}, Temp: {temperature}, Humidity: {humidity}")
# add wind fallback
wind_speed = weather_data.get("windspeed", 5)
url = "https://api.open-meteo.com/v1/forecast"
# add latitude & longitude keys
params["latitude"] = 13.08
params["longitude"] = 80.27
# ensure params dict exists
params = params if isinstance(params, dict) else {}
params["temperature_unit"] = "celsius"
# check API response keys
print("Keys:", data.keys())
# extract time info
time = weather_data.get("time", "N/A")
# add timestamp to output
print("Time:", time)
# cap temperature range
temperature = min(max(temperature, 0), 50)
# create config for API
API_TIMEOUT = 5
# use config timeout
response = requests.get(url, params=params, timeout=API_TIMEOUT)
# add retry count
RETRY_COUNT = 2
# basic retry logic
for _ in range(RETRY_COUNT):
    response = requests.get(url, params=params, timeout=API_TIMEOUT)

