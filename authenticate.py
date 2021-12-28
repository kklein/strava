import pickle

import yaml
from stravalib.client import Client

client = Client()


with open("auth.yaml") as filehandle:
    auth_data = yaml.safe_load(filehandle)


access_token = client.exchange_code_for_token(
    client_id=auth_data["client_id"],
    client_secret=auth_data["client_secret"],
    code=auth_data["code"],
)
with open("access_token.pickle", "wb") as f:
    pickle.dump(access_token, f)
