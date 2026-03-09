# --- Setup: The Mission Control Center ---
# A Dictionary (map) to store current resource levels
ship_resources = {
    "oxygen": 100,
    "fuel": 100,
    "food_rations": 50
}

# A List (array) to track the timeline of events
mission_log = ["Launched from Earth"]

# --- The Story Evolves: Deep Space Travel ---
# Finding a new moon adds a log entry
mission_log.append("Entered lunar orbit") # Operation: adding to a list

# A small leak occurs!
leak_amount = 15
ship_resources["oxygen"] -= leak_amount # Operation: modifying a dict value

# We find an old supply pod
found_rations = [5, 10, 5] # A list of small ration packs
ship_resources["food_rations"] += sum(found_rations) # Combining a list with a dict

# --- The Climax: Status Check ---
# Boolean check involving complex data access
low_fuel = ship_resources["fuel"] < 20
log_length = len(mission_log)

mission_log.append("Emergency check performed")

# --- Final Report ---
print(f"--- Mission Day {log_length} Report ---")
print(f"Log History: {mission_log}")
print(f"Current Supplies: {ship_resources}")

if ship_resources["oxygen"] > 50 and not low_fuel:
    print("Status: Mission is GO for deep space exploration.")
else:
    print("Status: Immediate return to base required!")