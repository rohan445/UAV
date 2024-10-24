import googlemaps

def get_distance(self, loc1, loc2):
    gmaps = googlemaps.Client(key='your_google_maps_api_key')
    result = gmaps.distance_matrix(loc1, loc2)['rows'][0]['elements'][0]
    return result['distance']['value'] / 1000  # Return distance in km

def display_route(self, loc1, loc2):
    map_url = f"https://www.google.com/maps/dir/{loc1}/{loc2}/"
    print(f"View the route here: {map_url}")
