import time  # 'time' module for timestamps
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

class DroneApp:
    def __init__(self):
        self.service_history = []  # Store flight history
        self.station_location = (-74.0060, 40.7128)  # Example station location (New York City)
    
    # Method to schedule a drone flight
    def flight(self):
        loc = input("Enter the delivery location (latitude, longitude): ").split(',')
        loc = (float(loc[1]), float(loc[0]))  # Parse as (longitude, latitude)
        dist = float(input("Enter the distance to the location (in km): "))
        wt = float(input("Enter the weight of the package delivered (in kg): "))
        duration = self.calc_time(dist)
        print(f"\nFlight scheduled\nLocation: {loc}\nArrival time: {duration} minutes")

        # Add flight to history
        self.drone_history(loc, dist, wt, duration)

    # Method to calculate flight time
    def calc_time(self, dist):
        speed = 70  # Speed in km/h
        duration = (dist / speed) * 60  # Convert hours to minutes
        return round(duration, 2)

    # Method to store flight history
    def drone_history(self, loc, dist, wt, duration):
        service = {
            "location": loc,
            "distance": dist,
            "weight": wt,
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration": duration
        }
        self.service_history.append(service)
        print("\nDrone flight added to the history")

    # Method to visualize all routes
    def visualize_routes(self):
        if not self.service_history:
            print("\nNo flight history available for visualization.")
        else:
            # Create GeoDataFrame for station and delivery locations
            station_gdf = gpd.GeoDataFrame(geometry=[Point(self.station_location)], crs="EPSG:4326")
            delivery_gdf = gpd.GeoDataFrame(geometry=[Point(flight['location']) for flight in self.service_history], crs="EPSG:4326")

            # Plot all routes
            fig, ax = plt.subplots(figsize=(10, 10))

            # Plot the station
            station_gdf.plot(ax=ax, color="green", markersize=100, label="Drone Station")

            # Plot delivery points and routes
            for flight in self.service_history:
                route = LineString([Point(self.station_location), Point(flight['location'])])
                route_gdf = gpd.GeoDataFrame(geometry=[route], crs="EPSG:4326")
                route_gdf.plot(ax=ax, color="blue", linewidth=2, label="Flight Route")

            # Plot the delivery locations
            delivery_gdf.plot(ax=ax, color="red", markersize=50, label="Delivery Locations")

            ax.set_title("All Drone Flight Routes", fontsize=16)
            plt.xlabel("Longitude")
            plt.ylabel("Latitude")

            plt.legend()
            plt.show()

    # Method to visualize a specific flight route
    def visualize_specific_route(self):
        if not self.service_history:
            print("\nNo flight history available for visualization.")
        else:
            print("\nSelect a flight to view its route:")
            for i, record in enumerate(self.service_history, 1):
                print(f"{i}. Location: {record['location']}, Distance: {record['distance']} km")

            # Ask the user to choose a flight
            flight_choice = int(input("\nEnter the flight number to display the route: ")) - 1

            if 0 <= flight_choice < len(self.service_history):
                selected_flight = self.service_history[flight_choice]
                display_route(self.station_location, selected_flight['location'])
            else:
                print("Invalid choice, please select a valid flight.")

    # Method to view flight history
    def service_view(self):
        if not self.service_history:
            print("\nNo History available, sorry")
        else:
            print("\nService History:")
            for i, record in enumerate(self.service_history, 1):
                print(f"{i}. Location: {record['location']}, Distance: {record['distance']} km, "
                      f"Weight: {record['weight']} kg, Flight time: {record['duration']} minutes")

    # Exit method
    def exit_service(self):
        print("\nExiting the App, Thank you!")
        exit(0)


# Function to display a specific route (helper function for single route visualization)
def display_route(station_location, delivery_location):
    route = LineString([Point(station_location), Point(delivery_location)])

    # Create GeoDataFrames for station and delivery location
    station_gdf = gpd.GeoDataFrame(geometry=[Point(station_location)], crs="EPSG:4326")
    delivery_gdf = gpd.GeoDataFrame(geometry=[Point(delivery_location)], crs="EPSG:4326")
    route_gdf = gpd.GeoDataFrame(geometry=[route], crs="EPSG:4326")

    # Plot the route and locations
    fig, ax = plt.subplots(figsize=(10, 10))

    route_gdf.plot(ax=ax, color="blue", linewidth=2, label="Flight Route")
    station_gdf.plot(ax=ax, color="green", markersize=100, label="Drone Station")
    delivery_gdf.plot(ax=ax, color="red", markersize=50, label="Delivery Location")

    ax.set_title("Drone Flight Route", fontsize=16)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.legend()
    plt.show()


# Display menu function
def display_menu():
    print("\nDrone Service Menu:")
    print("1. Schedule a Drone Flight")
    print("2. View Service History")
    print("3. View All Routes")
    print("4. View Specific Flight Route")
    print("5. Exit")


# Main function
def main():
    service = DroneApp()

    while True:
        display_menu()
        ch = input("Enter your choice (1-5): ")

        match ch:
            case '1':
                service.flight()  # Schedule a flight
            case '2':
                service.service_view()  # View service history
            case '3':
                service.visualize_routes()  # Visualize all routes
            case '4':
                service.visualize_specific_route()  # Visualize specific flight route
            case '5':
                service.exit_service()  # Exit the app
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


