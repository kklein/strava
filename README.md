Connect to Strava API, export data and analyze it.

# Steps
0. Follow [Strava's getting started guide](https://developers.strava.com/docs/getting-started/) to obtain `client_id`, `client_secret`, `access_token` and `refresh_token`. Copy all of those into `auth.yml`.
1. Web stuff: adapt `auth.yaml`.
2. Run `python authenticate.py`.
3. Run `python authorize.py`.
4. Run `python export.py`.
5. Run `jupyter notebook` and open `analysis.ipynb`.
