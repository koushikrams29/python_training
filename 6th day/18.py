
from fastapi import FastAPI, Request, HTTPException, Response
from typing import Any, Annotated
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import json
import random
import xml.etree.ElementTree as ET

app = FastAPI()

weather_data = [{'city': 'hyderabad', 'temperature': 33, 'pressure': 1010, 'wind_speeds': 13, 'aqi': 160, 'clouds': 0, 'probability of rain': 45}, {'city': 'kolkata', 'temperature': 17, 'pressure': 1007, 'wind_speeds': 16, 'aqi': 20, 'clouds': 75, 'probability of rain': 35}, {'city': 'vadodara', 'temperature': 27, 'pressure': 1022, 'wind_speeds': 4, 'aqi': 110, 'clouds': 85, 'probability of rain': 0}, {'city': 'chennai', 'temperature': 22, 'pressure': 1006, 'wind_speeds': 9, 'aqi': 20, 'clouds': 20, 'probability of rain': 40}, {'city': 'ahmedabad', 'temperature': 21, 'pressure': 1022, 'wind_speeds': 10, 'aqi': 120, 'clouds': 40, 'probability of rain': 5}, {'city': 'ahmedabad', 'temperature': 30, 'pressure': 1023, 'wind_speeds': 18, 'aqi': 110, 'clouds': 60, 'probability of rain': 80}, {'city': 'bengaluru', 'temperature': 20, 'pressure': 1015, 'wind_speeds': 11, 'aqi': 130, 'clouds': 100, 'probability of rain': 55}, {'city': 'thiruvananthapuram', 'temperature': 18, 'pressure': 1020, 'wind_speeds': 18, 'aqi': 150, 'clouds': 95, 'probability of rain': 70}, {'city': 'vadodara', 'temperature': 22, 'pressure': 1022, 'wind_speeds': 15, 'aqi': 130, 'clouds': 15, 'probability of rain': 90}, {'city': 'lucknow', 'temperature': 24, 'pressure': 1006, 'wind_speeds': 12, 'aqi': 200, 'clouds': 25, 'probability of rain': 60}, {'city': 'jaipur', 'temperature': 33, 'pressure': 1004, 'wind_speeds': 4, 'aqi': 110, 'clouds': 80, 'probability of rain': 30}, {'city': 'thiruvananthapuram', 'temperature': 21, 'pressure': 1023, 'wind_speeds': 11, 'aqi': 180, 'clouds': 50, 'probability of rain': 0}, {'city': 'visakhapatnam', 'temperature': 36, 'pressure': 1016, 'wind_speeds': 7, 'aqi': 20, 'clouds': 50, 'probability of rain': 15}, {'city': 'thiruvananthapuram', 'temperature': 27, 'pressure': 1018, 'wind_speeds': 4, 'aqi': 180, 'clouds': 75, 'probability of rain': 25}, {'city': 'thiruvananthapuram', 'temperature': 19, 'pressure': 1015, 'wind_speeds': 3, 'aqi': 140, 'clouds': 100, 'probability of rain': 65}, {'city': 'hyderabad', 'temperature': 25, 'pressure': 1013, 'wind_speeds': 12, 'aqi': 150, 'clouds': 20, 'probability of rain': 35}, {'city': 'kolkata', 'temperature': 29, 'pressure': 1020, 'wind_speeds': 18, 'aqi': 160, 'clouds': 0, 'probability of rain': 80}, {'city': 'mumbai', 'temperature': 26, 'pressure': 1018, 'wind_speeds': 18, 'aqi': 30, 'clouds': 0, 'probability of rain': 5}, {'city': 'vadodara', 'temperature': 25, 'pressure': 1017, 'wind_speeds': 18, 'aqi': 50, 'clouds': 40, 'probability of rain': 45}, {'city': 'bengaluru', 'temperature': 20, 'pressure': 1005, 'wind_speeds': 25, 'aqi': 180, 'clouds': 30, 'probability of rain': 35}, {'city': 'delhi', 'temperature': 20, 'pressure': 1022, 'wind_speeds': 9, 'aqi': 90, 'clouds': 35, 'probability of rain': 20}, {'city': 'kolkata', 'temperature': 23, 'pressure': 1008, 'wind_speeds': 20, 'aqi': 120, 'clouds': 65, 'probability of rain': 50}, {'city': 'jaipur', 'temperature': 21, 'pressure': 1006, 'wind_speeds': 13, 'aqi': 100, 'clouds': 100, 'probability of rain': 45}, {'city': 'ahmedabad', 'temperature': 23, 'pressure': 1007, 'wind_speeds': 18, 'aqi': 180, 'clouds': 55, 'probability of rain': 15}, {'city': 'vadodara', 'temperature': 22, 'pressure': 1011, 'wind_speeds': 23, 'aqi': 70, 'clouds': 60, 'probability of rain': 85}, {'city': 'bhopal', 'temperature': 33, 'pressure': 1018, 'wind_speeds': 16, 'aqi': 150, 'clouds': 95, 'probability of rain': 70}, {'city': 'thiruvananthapuram', 'temperature': 31, 'pressure': 1019, 'wind_speeds': 4, 'aqi': 190, 'clouds': 50, 'probability of rain': 35}, {'city': 'indore', 'temperature': 26, 'pressure': 1015, 'wind_speeds': 22, 'aqi': 190, 'clouds': 90, 'probability of rain': 20}, {'city': 'ahmedabad', 'temperature': 17, 'pressure': 1005, 'wind_speeds': 9, 'aqi': 180, 'clouds': 30, 'probability of rain': 40}, {'city': 'vadodara', 'temperature': 17, 'pressure': 1004, 'wind_speeds': 4, 'aqi': 200, 'clouds': 95, 'probability of rain': 50}]



# Get weather data for a city
def get_weather(city: str):
    for data in weather_data:
        if data.get("city").lower() == city.lower():
            return data
    return None

@app.get("/{city}")
@app.get("/{city}/{format}")
async def weather(city: str, format: str = "xml", request: Request = None):
    city_name = city
    format_type = format.lower()

    # Check if the city exists in weather data
    weather_out = get_weather(city_name)

    if weather_out is None:
        raise HTTPException(status_code=404, detail=f"City '{city_name}' not found")

    # Return JSON response
    if format_type == 'json':
        return JSONResponse(content=weather_out, status_code=200)

    # Return XML response
    elif format_type == 'xml':
        xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
        <data>
            <city>{weather_out['city']}</city>
            <temperature>{weather_out['temperature']}</temperature>
            <pressure>{weather_out['pressure']}</pressure>
            <wind_speeds>{weather_out['wind_speeds']}</wind_speeds>
            <aqi>{weather_out['aqi']}</aqi>
            <clouds>{weather_out['clouds']}</clouds>
            <probability_of_rain>{weather_out['probability of rain']}</probability_of_rain>
        </data>"""
        return Response(content=xml_response, media_type="application/xml", status_code=200)

    else:
        raise HTTPException(status_code=400, detail="Format not recognized. Supported formats: json, xml.")


