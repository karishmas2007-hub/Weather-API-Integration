import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

data = response.json()

print("\nWeather Report")
print("-------------------")


print("City:", city)
print("Temperature:", data["current_condition"][0]["temp_C"], "°C")
print("Weather:", data["current_condition"][0]["weatherDesc"][0]["value"])
print("Humidity:", data["current_condition"][0]["humidity"])