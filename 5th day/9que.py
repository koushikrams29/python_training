from flask import Flask , request, render_template, jsonify, Response
import random
import xml.etree.ElementTree as ET

app = Flask(__name__)

city_list = ["rajkot", "nashik", "udaipur", "mysuru", "ranchi",
                 "kanpur", "coimbatore", "varanasi", "bhubaneswar", "madurai"]

temp_values = [22, 33, 26, 24, 31, 29, 20, 25, 28, 30]
pressure_values = [1016, 1010, 1014, 1013, 1017, 1009, 1008, 1021, 1012, 1020]
wind_speed_values = [11, 5, 9, 16, 8, 13, 7, 4, 15, 10]
humidity_levels = [72, 55, 62, 83, 49, 78, 61, 88, 57, 43]
clouds_cover_values= [25, 60, 45, 35, 75, 80, 50, 40, 20, 90]
visibility_levels = [10, 12, 8, 7, 15, 11, 9, 13, 6, 14]
air_quality_index= [65, 120, 80, 45, 95, 110, 70, 85, 100, 150]
rain_probability= [40, 60, 25, 35, 50, 30, 45, 75, 20, 10]

def generate_weather_data():
    return {
        'city': random.choice(city_list),
        'temperature': random.choice(temp_values),
        'pressure': random.choice(pressure_values),
        'wind_speed': random.choice(wind_speed_values),
        'humidity': random.choice(humidity_levels),
        'cloud_cover': random.choice(clouds_cover_values),
        'visibility': random.choice(visibility_levels),
        'aqi': random.choice(air_quality_index),
        'rain_probability': random.choice(rain_probability)
    }


weather_info = [generate_weather_data() for i in range(20)]

#print(weather_info[0]['city'])

def fetch_weather_data(city_name):
    for data in weather_info:
        if data.get("city") == city_name:
            return data


@app.route("/<string:city_name>", methods=['GET'])
@app.route("/<string:city_name>?<string:data_format>/", methods=['GET'])
def weather(city_name, data_format="xml"):
    formatted_city = city_name
    formatted_format = data_format
    if request.method == 'GET':
        formatted_city = request.args.get('city', city_name)
        formatted_format = request.args.get('format', data_format)
    else:
        if 'Content-Type' in request.headers:
            if request.headers['Content-Type'] in ['application/json']:
                formatted_city = request.json.get('city', city_name)
                formatted_format = request.json.get('format', data_format)
            elif request.headers['Content-Type'] in ['application/xml']:
                root = ET.fromstring(request.data)
                element = root.findall("./name")
                if element:
                    formatted_city = element[0].text
                else:
                    formatted_city = city_name
                formatted_format = "xml"
            else:
                return "Content type not recognized"
    weather_details = fetch_weather_data(city_name.lower())
    if formatted_format == 'json':
        if city_name is not None:
            return jsonify(weather_details)
        else:
            response = 'Error'
            response.status_code = 500
        return response
    elif formatted_format == 'xml':
        xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
        <data>
            <city>{weather_details['city']}</city>
            <temperature>{weather_details['temperature']}</temperature>
            <pressure>{weather_details['pressure']}</pressure>
            <wind_speed>{weather_details['wind_speed']}</wind_speed>
            <humidity>{weather_details['humidity']}</humidity>
            <cloud_cover>{weather_details['cloud_cover']}</cloud_cover>
            <visibility>{weather_details['visibility']}</visibility>
            <aqi>{weather_details['aqi']}</aqi>
            <rain_probability>{weather_details['rain_probability']}</rain_probability>
        </data>"""
        return Response(response=xml_response, status=200, mimetype="application/xml")
    else:
        return "Format not recognized"

if __name__ == '__main__':
    app.run()