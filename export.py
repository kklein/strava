import datetime
import pickle

import pandas as pd
import yaml
from stravalib.client import Client

with open("auth.yaml") as filehandle:
    auth_data = yaml.safe_load(filehandle)

client = Client()

with open("access_token.pickle", "rb") as f:
    access_token = pickle.load(f)

client.access_token = access_token["access_token"]
client.refresh_token = access_token["refresh_token"]
client.token_expires_at = access_token["expires_at"]


athlete = client.get_athlete()
print(
    "Athlete's name is {} {}, based in {}, {}".format(
        athlete.firstname, athlete.lastname, athlete.city, athlete.country
    )
)

start_date = datetime.datetime(2020, 1, 1)

activities = client.get_activities(after=start_date)

cols = [
    "name",
    "start_date_local",
    "type",
    "distance",
    "moving_time",
    "elapsed_time",
    "total_elevation_gain",
    "elev_high",
    "elev_low",
    "average_speed",
    "max_speed",
    "average_heartrate",
    "max_heartrate",
    "start_latitude",
    "start_longitude",
]

data = []
for activity in activities:
    my_dict = activity.to_dict()
    data.append([activity.id] + [my_dict.get(x) for x in cols])

# Add id to the beginning of the columns, used when selecting a specific activity
cols.insert(0, "id")
df = pd.DataFrame(data, columns=cols)
df.to_pickle("strava_data.pickle")
