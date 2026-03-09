# --- Setup: Our Initial State ---
customer_name = "Alex"           # String
wallet_balance = 15.50           # Number (Float)
is_morning_rush = True           # Boolean

print(customer_name + " walks into the coffee shop.")

# --- The Story Evolves ---
coffee_price = 5.25
service_fee = 1.50
total_cost = coffee_price + service_fee  # Operation on numbers

# Check if we can afford it and if it's too busy
can_afford = wallet_balance >= total_cost   # Boolean operation
will_wait_in_line = not is_morning_rush     # Boolean operation (NOT)

print("Total price is: $" + str(total_cost))

# --- The Climax: Decision making ---
if can_afford and (will_wait_in_line or wallet_balance > 20):
    wallet_balance -= total_cost            # Updating a number
    is_happy = True                         # Boolean assignment
    status_message = "Success! Enjoy the caffeine."
else:
    is_happy = False
    status_message = "Maybe tomorrow..."

# --- Conclusion ---
print(customer_name + "'s status: " + status_message)
print("Remaining funds: $" + str(wallet_balance))
print("Is " + customer_name + " caffeinated? " + str(is_happy))