import http.client
import json

with open ("secret.api.json", "r") as f:
    secret_data = json.load(f)

api_key = secret_data["api"]

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': api_key
    }

conn.request("GET", "/gasPrice/turkeyGasoline?district=kadikoy&city=istanbul", headers=headers)

res = conn.getresponse()
data = res.read()

response_data = json.loads(data)

for station in response_data["result"]:
    if station["marka"] == "Shell":
        price = station["benzin"]
        break
else:
    price = None

if price is not None:
    print("Gasoline price in Kadikoy, Istanbul (Shell station):", price)
else:
    print("Shell station not found or no price information available.")


def calculate_fuel_consumption(total_km, liters_per_100_km):
    return (total_km / 100) * liters_per_100_km

def calculate_and_print(total_km, liters_per_100_km, price):
    total_fuel_consumption = calculate_fuel_consumption(total_km, liters_per_100_km)
    total_cost = total_fuel_consumption * price
    
    print(f"You have traveled {total_km} kilometers, and your vehicle has consumed {total_fuel_consumption:.2f} liters of fuel. Total cost of the trip: {total_cost:.2f}")

def main():
    try:
        aydin_to_istanbul_total_km = 547
        istanbul_to_igneada_total_km = 262
        aydin_to_istanbul_igneada_total_km = 809
        liters_per_100_km = 7.5
        
        print("Traveling from Aydin to Istanbul:")
        calculate_and_print(aydin_to_istanbul_total_km, liters_per_100_km, price)

        print("\nTraveling from Istanbul to Igneada:")
        calculate_and_print(istanbul_to_igneada_total_km, liters_per_100_km, price)

        print("\nTraveling from Aydin to Igneada:")
        calculate_and_print(aydin_to_istanbul_igneada_total_km, liters_per_100_km, price)

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
