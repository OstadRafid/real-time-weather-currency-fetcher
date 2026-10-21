import os
import niquests
from datetime import datetime
import json
from dotenv import load_dotenv
load_dotenv()

GET_API = os.getenv("GET_API")

def Weather():
    print()
    print("<================== Current Weather ==================>".center(110))
    City_Name = input("Enter City Name -> ")
    print()
    URL = f"http://api.weatherapi.com/v1/current.json?key={GET_API}&q={City_Name}"

    Response = niquests.get(URL)
    Data = Response.json()

    city_name = Data["location"]["name"]
    Country_Name = Data["location"]["country"]
    Temperature = Data["current"]["temp_c"]
    Humidity = Data["current"]["humidity"]
    Wind_Speed = Data["current"]["wind_kph"]
    Weather_condition = Data["current"]["condition"]["text"]
    Local_Time_Date = datetime.strptime(Data["location"]["localtime"], "%Y-%m-%d %H:%M").strftime("%d-%B-%Y | %A | %I:%M:%S %p")

    print("<==================== Weather Report ====================>")
    print(f"\nCity -> {city_name}")
    print(f"Country Name -> {Country_Name}")
    print(f"Temperature -> {Temperature}")
    print(f"Humidity -> {Humidity}")
    print(f"Wind Speed -> {Wind_Speed}")
    print(f"Weather Condition -> {Weather_condition}")
    print(f"Fetched_At -> {Local_Time_Date}\n")
    print("==========================================================\n")

    Result_Data = {
    "type": "weather",
    "city": city_name,
    "country": Country_Name,
    "temperature": Temperature,
    "humidity": Humidity,
    "wind_speed": Wind_Speed,
    "condition": Weather_condition,
    "time": Data["location"]["localtime"]
    }
    
    try:
        with open("data.json", "r") as File:
            Saved_Data = json.load(File)
    except (FileNotFoundError, json.JSONDecodeError):
        
        Saved_Data = []
        
        Saved_Data.append(Result_Data)
        
        with open("data.json", "w") as File:
            json.dump(Saved_Data, File, indent=4)
            
        print("Data saved successfully!")

Weather()