import pandas as pd
import requests

# Load data (adjust the path as needed)
df = pd.read_csv('yellow_tripdata_2015-01.csv')

# Sample a portion of the data
df_sample = df.sample(n=1000)

# Google Maps API key
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'  # Replace with your API key

# Function to get driving distance using Google Maps Distance Matrix API
def get_driving_distance(pickup_coords, dropoff_coords):
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={pickup_coords[0]},{pickup_coords[1]}&destinations={dropoff_coords[0]},{dropoff_coords[1]}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            # Extract distance from the response
            distance = data['rows'][0]['elements'][0]['distance']['value']  # Distance in meters
            return distance / 1000  # Convert to kilometers
        except (IndexError, KeyError):
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Add a new column for driving distance
df_sample['driving_distance_km'] = df_sample.apply(
    lambda row: get_driving_distance((row['pickup_latitude'], row['pickup_longitude']),
                                      (row['dropoff_latitude'], row['dropoff_longitude'])),
    axis=1
)

# Display the results
print(df_sample[['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude', 'driving_distance_km']])
