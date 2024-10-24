import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

# Define the coordinates of the drone station (starting point)
station_location = (-74.0060, 40.7128)  # Example: New York City coordinates (longitude, latitude)

# List of delivery locations (longitude, latitude)
delivery_locations = [
    (-73.9680, 40.7851),  # Central Park
    (-73.9855, 40.7580),  # Times Square
    (-73.9967, 40.7061),  # Brooklyn Bridge
    (-74.0445, 40.6892),  # Statue of Liberty
    (-73.9857, 40.7484)   # Empire State Building
]

# Create GeoDataFrame for the delivery locations
delivery_points = [Point(lon, lat) for lon, lat in delivery_locations]

# Create a GeoDataFrame to store flight routes (lines from station to each delivery location)
routes = [LineString([Point(station_location), Point(dest)]) for dest in delivery_locations]

# Convert the routes into a GeoDataFrame
routes_gdf = gpd.GeoDataFrame(geometry=routes)

# Create GeoDataFrame for the station location
station_gdf = gpd.GeoDataFrame(geometry=[Point(station_location)], crs="EPSG:4326")

# Plot the routes and the points
fig, ax = plt.subplots(figsize=(10, 10))

# Plot delivery routes
routes_gdf.plot(ax=ax, color="blue", linewidth=2, label="Flight Route")

# Plot delivery locations
gpd.GeoDataFrame(geometry=delivery_points).plot(ax=ax, color="red", markersize=50, label="Delivery Locations")

# Plot the drone station
station_gdf.plot(ax=ax, color="green", markersize=100, label="Drone Station")

# Set title and labels
ax.set_title("Drone Delivery Flight Routes", fontsize=16)
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Add a legend
plt.legend()

# Show the plot
plt.show()
