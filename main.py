import googlemaps
import pandas as pd
from tqdm import tqdm
import time


gmaps = googlemaps.Client(key='')


sw = (13.6781032056605604, 100.45549562624741)
ne = (13.803338273670649, 100.54202626602314)


step = 0.011
radius = 1000  

data = pd.DataFrame(columns=['Name', 'Address', 'Latitude', 'Longitude', 'Rating'])

lat_steps = int((ne[0] - sw[0]) / step)
lng_steps = int((ne[1] - sw[1]) / step)

for i in tqdm(range(lat_steps)):
    lat = sw[0] + i * step
    for j in range(lng_steps):
        lng = sw[1] + j * step

        places_result = gmaps.places_nearby(location=(lat, lng), radius=radius, type='bar')

        if 'results' in places_result:
            for place in places_result['results']:
                name = place.get('name')
                address = place.get('vicinity')
                lat = place['geometry']['location']['lat']
                lng = place['geometry']['location']['lng']
                rating = place.get('rating', None)

                data = pd.concat([data, pd.DataFrame({'Name': [name], 'Address': [address], 'Latitude': [lat], 'Longitude': [lng], 'Rating': [rating]})],
                                 ignore_index=True)

        time.sleep(0.2)

data.drop_duplicates(subset=['Name', 'Address', 'Latitude', 'Longitude'], keep='first', inplace=True)
data.to_excel('bars_info.xlsx', index=False)

