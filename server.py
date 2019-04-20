#author: Zeshen Li
#date: 4/19/2019

import os
from flask import Flask, request, render_template, g, redirect, Response
import requests
import json

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

api = "f84cada401722828cdbbb47fe654568c"
api_key = "&appid=" + api
current_weather_data = "http://api.openweathermap.org/data/2.5/weather?q="
hourly_forecast = "http://api.openweathermap.org/data/2.5/forecast/hourly?q="
hf_mode = "&mode=json"

@app.route('/')
def home():

	return render_template("home.html")

@app.route('/weather',methods=['POST'])
def weather():
	city_name = request.form['name']
	#current weather data
	current_weather_data_query = current_weather_data + city_name + api_key
	resp = requests.get(current_weather_data_query)
	dict = resp.json()
	cod = dict["cod"]
	#check if input is valid
	if (cod == 200):
		cw_data = {}
		cw_data["weather"] = dict["weather"][0]["main"]
		cw_data["description"] = dict["weather"][0]["description"]
		cw_data["temp"] = round(dict["main"]["temp"]-273.15,2)
		cw_data["pressure"] = dict["main"]["pressure"]
		cw_data["humidity"] = dict["main"]["humidity"]
		cw_data["temp_min"] = round(dict["main"]["temp_min"]-273.15,2)
		cw_data["temp_max"] = round(dict["main"]["temp_max"]-273.15,2)
	else:
		return render_template("error.html")
	#hourly forecast
	hourly_forecast_query = hourly_forecast + city_name + hf_mode + api_key
	resp = requests.get(hourly_forecast_query)
	dict = resp.json()
	cod = dict["cod"]
	#check if input is valid
	if (cod == "200"):
		list = dict["list"]
		hf_data = {}
		#put desired data into list
		hf_data["temp"] = []
		hf_data["temp_min"] = []
		hf_data["temp_max"] = []
		hf_data["weather"] = []
		hf_data["date"] = []
		for x in list:
			hf_data["temp"].append(round(x["main"]["temp"]-273.15,2))
			hf_data["temp_min"].append(round(x["main"]["temp_min"]-273.15,2))
			hf_data["temp_max"].append(round(x["main"]["temp_max"]-273.15,2))
			hf_data["weather"].append(x["weather"][0]["main"])
			hf_data["date"].append(x["dt_txt"])
		
		#convert list into string
		hf_data["str_temp"] = ""
		hf_data["str_temp_min"] = ""
		hf_data["str_temp_max"] = ""
		hf_data["str_weather"] = ""
		hf_data["str_date"] = ""
		for i in range(len(list)):
			hf_data["str_temp"] = hf_data["str_temp"] + str(hf_data["temp"][i]) + ","
			hf_data["str_temp_min"] = hf_data["str_temp_min"] + str(hf_data["temp_min"][i]) + ","
			hf_data["str_temp_max"] = hf_data["str_temp_max"] + str(hf_data["temp_max"][i]) + ","
			hf_data["str_weather"] = hf_data["str_weather"] + str(hf_data["weather"][i]) + ","
			hf_data["str_date"] = hf_data["str_date"] + str(hf_data["date"][i]) + ","
	else:
		return render_template("error.html")
	return render_template("weather.html", cw_data = cw_data, hf_data = hf_data, city_name = city_name)

@app.route('/goback', methods=['POST'])	
def goback():
	return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)