# Ethan Mayer
# Feb. 5th, 2026

trip_durations = {1.1, 0.8, 2.5, 2.6, 3.0}
trip_fare = {6.25, 5.25, 10.50, 8.05, 12.00}

trips = dict(zip(trip_durations, trip_fare))
print(trips)

trip_num = input("What trip do you want? [1-4]: ")
trip_index = int(trip_num) - 1
print(f"Duration: {list(trips.keys())[trip_index]} miles")
print(f"Fare: ${list(trips.values())[trip_index]:.2f}")
