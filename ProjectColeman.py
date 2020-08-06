'''
Mia Coleman
August 9, 2020
CIS 245
Class Project: Final Draft

This program prompts the user for their city or zip code in the function getData(). The function
getWeather requests data from openweathermap.org. The weather for the location given is displayed 
using the displayWeather function. If user input is invalid, an error message is displayed and the
program prompts the user again. The user will be prompted for city/zip code until a '0' is entered.
'''

import requests
import json

def getData():
# Function getData() gets the user input. Exits program when user enters "0".
	print("\nWhat's the weather? ")
	place = input("Enter your city, zip code or '0' to exit: ")

	if place == "0":
		exit()
	else:
		return place

def getWeather(place):
# Function getWeather requests data from openweathermap.org
	print("\n...requesting...")

	apiKey = "62e15907d03bb90ea449be0d9336566d"

	# try block for connection success/failure
	try:
	# Try: using location as a US city name.
		urlC = "http://api.openweathermap.org/data/2.5/weather?q="+place+",US&units=imperial&appid="+apiKey
	
		rC = requests.get(urlC)

		print("Connection successful!\n")
		return json.loads(rC.text)
	except:
	# Except: using location as a US zip code.
		urlZ = "http://api.openweathermap.org/data/2.5/weather?zip="+place+",US&units=imperial&appid="+apiKey
	
		rZ = requests.get(urlZ)

		print("Connection successful!\n")
		return json.loads(rZ.text)
	else:
		print("Connection failed")

def displayWeather(weatherData):
# Function displayWeather formats the weather data recieved from openweathermap.org
	print("For city: ", weatherData['name'])
	print("Temperature:",weatherData['main']['temp'],"°F")
	print("Feels like:",weatherData['main']['feels_like'],"°F")
	print("Wind speed:",weatherData['wind']['speed'],"mph", weatherData['wind']['deg'],"deg")
	print("Pressure:",weatherData['main']['pressure'],"hPa")
	print("Humidity:",weatherData['main']['humidity'],"%")
	print("Weather:",weatherData['weather'][0]['main'])
	print("Weather description:",weatherData['weather'][0]['description']) 

def main():
# Main function

	location = getData()
	# Calls getData() function

	while location != "0":
	# Loops until 0 is entered by the user
		
		# Try block for location validation.
		try:
			weatherData = getWeather(location)
			displayWeather(weatherData)
		except:
			print("ERROR: Invalid Entry!!")

		location = getData()

if __name__ == "__main__":
	main()
