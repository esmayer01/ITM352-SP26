# Ethan Mayer
# Feb. 5th, 2026

trip_durations = {1.1, 0.8, 2.5, 2.6}
trip_fare = {6.25, 5.25, 10.50, 8.05,}

# Create a list of dictionaries where each dictionary represents a trip

trips_list = [
    {"duration": 1.1, "fare": 6.25},
    {"duration": 0.8, "fare": 5.25},
    {"duration": 2.5, "fare": 10.50},
    {"duration": 2.6, "fare": 8.05},
]

# trips = dict(zip(trip_durations, trip_fare))
# print(trips)

trip_num = input("What trip do you want? [1-4]: ")
trip_index = int(trip_num) - 1

print(f"Duration: {trips_list[trip_index]['duration']} miles")
print(f"Fare: ${trips_list[trip_index]['fare']:.2f}")
# print(f"Duration: {list(trips.keys())[trip_index]} miles")
# print(f"Fare: ${trips_list[trip_index]['fare']:.2f}")
