import json
import datetime
import os

import requests

from spotifyapi.api_constants import DATA_DIR
        
def get_new_access_token(client_id, client_secret, timeout=60, retries=3) -> str:
    """Utily function called by get_access_token() to get a new access token without checking for an existing token file.

    This is a utility function. Users should instead use get_access_token(). Provided a client ID and client secret, this function will query the Spotify API for a new access token. If the request
    is successful, it will calculate the expire time and return the response data. If the request fails, it will print an
    error and return None. If the request times out, it will retry the request up to the number of retries specified. If
    the request is successful, but the status code is not 200, it will print an error and return None.

    Args:
        client_id: A user's Spotify client ID (from the Spotify Developer Dashboard).
        client_secret: A user's Spotify client secret (from the Spotify Developer Dashboard).
        timeout: The number of seconds to wait for the server to send data before giving up and retrying.
        retries: The maximum number of retries to attempt if the request fails before throwing an exception.

    Returns:
        A valid access token from the Spotify API as a string.

    Raises:
        TimeoutError: If the request times out.
        RequestException: If the request fails (the status code is not 200).

    Example:
        >>> access_token = spotifyapi.get_new_access_token(client_id, client_secret, timeout=60, retries=3)
    """

    ## Define API endpoint and data
    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    for i in range(retries):
        try:
            ## Query API
            response = requests.post(url, headers=headers, data=data, timeout=timeout)

            if response.status_code == 200:
                ## If request is successful, calc expire time and return response data
                print('API request succeeded!')
                print(response.json())
                res_data = response.json()

                ## Calculate expire time from expires_in parameter (which is in seconds)
                res_data['expire_date'] = datetime.datetime.now().timestamp() + response.json()['expires_in']

                return res_data
            else:
                ## Otherwise, print error
                print(f'Request failed. Expected 200, got {response.status_code}: {response.text}')
                return None
        except requests.exceptions.Timeout as e:
            print(f'API request timed out: {e}')
            continue
        except requests.exceptions.RequestException as e:
            print(f'An error occurred during the request: {e}')
            return None
        
    print('Failed to get access token.')
    return None

def get_access_token(client_id: str, client_secret: str, timeout:float=60, retries:int=3) -> str:
    """Gets a valid access token from the Spotify API.

    Provided a client ID and client secret, this function will get a valid access
    token from the Spotify API. If a token file exists, it will check if the
    token is expired. If the token is expired, it will get a new token and
    overwrite the existing token file.  If the token file does not exist, it will
    get a new token and write it to a new token file.

    Args:
        client_id: A user's Spotify client ID (from the Spotify Developer Dashboard).
        client_secret: A user's Spotify client secret (from the Spotify Developer Dashboard).
        timeout: The number of seconds to wait for the server to send data before giving up and retrying.
        retries: The maximum number of retries to attempt if the request fails before throwing an exception.

    Returns:
        A valid access token from the Spotify API as a string.

    Raises:
        TimeoutError: If the request times out.
        RequestException: If the request fails (the status code is not 200).

    Example:
        >>> access_token = spotifyapi.get_access_token(client_id, client_secret, timeout=60, retries=3)
    """

    token_file_path = f'{DATA_DIR}/access_token.json'

    def get_write_token(path):
        response = get_new_access_token(
                client_id = client_id, 
                client_secret = client_secret,
                timeout = timeout,
                retries = retries)

        with open(path, 'w') as token_file:
                json.dump(response, token_file)

        return response['access_token']

    ## Check if token file exists
    if not os.path.exists(token_file_path):
        print(f'{token_file_path} not found. Creating file and getting new token...')
        return get_write_token(token_file_path)
    else:
        try:
            with open(token_file_path, 'r') as token_file:
                data = json.load(token_file)

            ## If token expires in the next 2 minutes, get new token
            if data['expire_date'] < datetime.datetime.now().timestamp() + 120:
                ## Get new token and write to file
                print('Token expired. Getting new token...')
                return get_write_token(token_file_path)
            else:
                ## Otherwise, get existing token
                print('Using existing token...')
                return data['access_token']
        except FileNotFoundError:
            print(f'{token_file_path} not found.')

