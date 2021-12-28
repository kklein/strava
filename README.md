Connect to Strava API, export data and analyze it.

# Steps
1. Follow [Strava's getting started guide](https://developers.strava.com/docs/getting-started/) to obtain `client_id`, `client_secret`, `access_token` and `refresh_token`. Copy all of those into `auth.yml`.
2. Run `python authorize.py`. Follow the CLI instructions and copy the `code` into `auth.yml`.
3. Run `python authenticate.py`.
4. Run `python export.py`.
5. Run `jupyter notebook` and open `analysis.ipynb`.

# Todos
* Figure out a way to refresh the `access_token`.
