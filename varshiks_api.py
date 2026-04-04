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