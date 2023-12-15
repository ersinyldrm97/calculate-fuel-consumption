def calculate_fuel_consumption(total_km, liters_per_100_km):
    return (total_km / 100) * liters_per_100_km

def calculate_and_print(total_km, liters_per_100_km, petrol_price):
    total_fuel_consumption = calculate_fuel_consumption(total_km, liters_per_100_km)
    total_cost = total_fuel_consumption * petrol_price
    
    print(f"You have traveled {total_km} kilometers, and your vehicle has consumed {total_fuel_consumption:.2f} liters of fuel. Total cost of the trip: {total_cost:.2f}")

def main():
    try:
        aydin_to_istanbul_total_km = 550
        istanbul_to_igneada_total_km = 262
        aydin_to_istanbul_igneada_total_km = 809
        liters_per_100_km = 7.5
        petrol_price = 33.89
        
        print("Traveling from Aydin to Istanbul:")
        calculate_and_print(aydin_to_istanbul_total_km, liters_per_100_km, petrol_price)

        print("\nTraveling from Istanbul to Igneada:")
        calculate_and_print(istanbul_to_igneada_total_km, liters_per_100_km, petrol_price)

        print("\nTraveling from Aydin to Igneada:")
        calculate_and_print(aydin_to_istanbul_igneada_total_km, liters_per_100_km, petrol_price)

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
