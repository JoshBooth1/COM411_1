print("How many bars should be charged?")
bars_to_charge = int(input())

bars_charged = 0

while bars_to_charge > bars_charged:
    print(f"Charging: {'█' * bars_charged}")
    bars_charged = bars_charged + 1

print("Battery is fully charged")
