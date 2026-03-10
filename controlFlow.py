import random

# 1. DATA TYPES & STRUCTURES
# Modeling a city's weather over a 3-day 'evolution'
# We use a LIST of DICTIONARIES to model the passage of time.
weather_forecast = [
    {"day": "Monday", "temp": 72, "is_sunny": True, "conditions": ["windy", "dry"]},
    {"day": "Tuesday", "temp": 65, "is_sunny": False, "conditions": ["rainy", "humid"]},
    {"day": "Wednesday", "temp": 82, "is_sunny": True, "conditions": ["hot", "calm"]}
]

city_name = "Pythonia"  # String
target_temp = 75        # Number
is_simulation_active = True  # Boolean

print(f"--- Starting Weather Simulation for {city_name} ---")

# 2. LOOPS (Control Flow)
# We loop through the list to see how the phenomenon 'evolves' each day
for forecast in weather_forecast:
    print(f"\nForecast for {forecast['day']}:")
    
    # Accessing nested data (a List inside a Dictionary)
    print("Specific conditions today:")
    for detail in forecast['conditions']:
        print(f"- {detail}")

    # 3. CONDITIONALS (Control Flow)
    # Using the data to make 'decisions' in the code
    if forecast['temp'] > target_temp:
        print(f"Result: It's hotter than {target_temp} degrees. Wear shorts!")
    elif forecast['temp'] == target_temp:
        print(f"Result: It's exactly {target_temp} degrees. Perfect weather.")
    else:
        print(f"Result: It's a bit chilly. Bring a jacket.")

    # Combining Boolean logic with a Conditional
    if forecast['is_sunny'] and "windy" in forecast['conditions']:
        print("Note: Watch out, the sun is out but it's breezy!")

print("\n--- Simulation Complete ---")