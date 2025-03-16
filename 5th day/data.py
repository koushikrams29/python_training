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

print(weather_info[0]['city'])