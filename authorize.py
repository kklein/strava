import yaml
from stravalib.client import Client

client = Client()

with open("auth.yaml") as filehandle:
    auth_data = yaml.safe_load(filehandle)

url = client.authorization_url(
    client_id=auth_data["client_id"],
    redirect_uri="http://127.0.0.1:5000/authorization",
    scope=["read_all", "profile:read_all", "activity:read_all"],
)
print(
    """
    Visit the following url in your browser.
    You will be asked to authenticate and authorize access to strava.
    Afterwards, you will be redirected to a url with an
    `ERR_CONNECTION_REFUSED` error. Invesitgate the url and extract
    the code between `code=` and `&scope=`.
    Copy this code into your auth.yml.
    """
)

print(url)
