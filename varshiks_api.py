def get_weather_data(city):
    api_key = "74eb35dc87ea251ffb73b2ce2becbae0"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # DEBUG PRINT (helps you understand errors)
        print(data)

        if response.status_code == 200 and "main" in data:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            rainfall = data.get('rain', {}).get('1h', 0)

            return temp, humidity, rainfall
        else:
            print("API Error:", data)
            return None, None, None

    except Exception as e:
        print("Exception:", e)
        return None, None, None

def predict_crops(input_data):
    input_df = pd.DataFrame([input_data], columns=feature_names)
    probabilities = model.predict_proba(input_df)[0]

    le = load_encoder()

    # FIX: use label encoder
    crop_names = le.inverse_transform(np.arange(len(probabilities)))

    crop_confidences = [(crop, prob * 100) for crop, prob in zip(crop_names, probabilities)]
    
    return sorted(crop_confidences, key=lambda x: x[1], reverse=True)

def get_crops_by_season(season):
    """Get all crops that belong to a season"""
    return [crop for crop in all_crops if crop_seasons.get(crop) == season]

def get_confidence_level(confidence):
    """Get confidence level class"""
    if confidence >= 90:
        return "conf-high"
    elif confidence >= 70:
        return "conf-moderate"
    else:
        return "conf-low"
        # add user agent header
headers = {"User-Agent": "crop-predictor-app"}
response = requests.get(url, params=params, headers=headers)
# check response content
if not data:
    print("Empty API response received")
    # strip unwanted values
temperature = abs(temperature)
# ensure humidity integer
humidity = int(humidity)
# handle negative wind speed
wind_speed = max(wind_speed, 0)
# add simple validation
if temperature == 0:
    print("Warning: Temperature value seems incorrect")
# add API response time log
import time
start_time = time.time()
# calculate response time
end_time = time.time()
print("Response Time:", end_time - start_time)
# add simple validation
if temperature == 0:
    print("Warning: Temperature value seems incorrect")
    # ensure crop name string
crop_name = str(crop_name)
# ensure rainfall is non-negative
rainfall = max(rainfall, 0)