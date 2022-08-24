from configparser import ConfigParser


def _get_api_key():
    """
    Fetch the API key from your configuration file
    Expects a configuration file named 'secretes.ini' with structure:
    [openweather]
    api_key=<openweather-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]
