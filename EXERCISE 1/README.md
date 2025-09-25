import array

# Suppose we record the number of buses on each route
bus_counts = [12, 15, 10, 18, 20]  # Number of buses per route

total_buses = sum(bus_counts)
average_buses = total_buses / len(bus_counts)
min_buses = min(bus_counts)
max_buses = max(bus_counts)

# Strings
report = (
    f"Total Buses Scheduled: {total_buses}\n"
    f"Average Buses per Route: {average_buses:.2f}\n"
    f"Minimum Buses on a Route: {min_buses}\n"
    f"Maximum Buses on a Route: {max_buses}\n"
)
print("=== Bus Route Report ===")
print(report)

# Booleans
# Apply threshold condition
threshold = 14
if average_buses > threshold and max_buses > 15:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists
# List of route names
routes = ['Route A', 'Route B', 'Route C', 'Route D', 'Route E']
print("\nRoutes (Before Modifications):", routes)

# Add a new route
routes.append('Route F')

# Remove a route with less than 11 buses
for i, count in enumerate(bus_counts):
    if count < 11:
        removed = routes.pop(i)
        print(f"Removed '{removed}' due to low bus count (<11).")
        break

# Sort and display
routes.sort()
print("Routes (After Modifications):", routes)

# Arrays
# Store a fixed-size subset of bus_counts (first 4 routes)
bus_array = array.array('i', bus_counts[:4])
array_sum = sum(bus_array)
list_sum = sum(bus_counts[:4])
print(f"\nSum from array: {array_sum}")
print(f"Sum from list subset: {list_sum}")

# Dictionaries
# Create list of dictionaries for each route
route_data = [
    {'id': 1, 'name': 'Route A', 'value': 12},
    {'id': 2, 'name': 'Route B', 'value': 15},
    {'id': 3, 'name': 'Route C', 'value': 10},
    {'id': 4, 'name': 'Route D', 'value': 18},
    {'id': 5, 'name': 'Route E', 'value': 20}
]

# Update value of Route B
for route in route_data:
    if route['name'] == 'Route B':
        route['value'] = 17
        print("\nUpdated Route B's bus count to 17.")

# Delete Route C
route_data = [route for route in route_data if route['name'] != 'Route C']
print("Deleted Route C from the route data.")

# Compute total bus count from all route data
total_value = sum(route['value'] for route in route_data)
print(f"Total Buses (from route data): {total_value}")

