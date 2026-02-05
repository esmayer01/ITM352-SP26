# Ethan Mayer
# Feb. 5th, 2026

trip_durations = {1.1, 0.8, 2.5, 2.6, 3.0}
trip_fare = {6.25, 5.25, 10.50, 8.05, 12.00}

taxiTrips = {
    "miles": trip_durations,
    "fare": trip_fare,
}

print(taxiTrips)

print(f"The third trip was {list(taxiTrips['miles'])[2]} miles long")
print(f"The fare for the third trip was ${taxiTrips['fare'][2]}.")