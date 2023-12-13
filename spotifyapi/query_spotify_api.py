import requests
from spotifyapi.api_constants import ARTISTS_ENDPOINT, AUDIO_FEATURES_ENDPOINT

## Base API querying function for others to build on
def query_spotify(endpoint: str, access_token: str, timeout: float=60, retries: int=3) -> dict or None:
    
    """
    Query the Spotify API at the specified endpoint.

    Args:
        endpoint (str): The API endpoint to query.
        access_token (str): Spotify access token for authentication.
        timeout (int, optional): Maximum time (in seconds) to wait for the request to complete. Defaults to 60.
        retries (int, optional): Number of retry attempts in case of failure. Defaults to 3.

    Returns:
        dict or None: The JSON response from the Spotify API if the request is successful, 
                     otherwise returns None.

    Example:
        >>> endpoint = 'https://api.spotify.com/v1/tracks/3Hvu1pq89dGspIjqBBMIsU'
        >>> access_token = 'your_spotify_access_token'
        >>> track_info = spotifyapi.query_spotify(endpoint, access_token)
    """    
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    for i in range(retries):
        ## Handle timeout errors after 1 minute
        try:
            response = requests.get(endpoint, headers=headers, timeout=timeout)

            if response.status_code == 200:
                print('API request succeeded!')
                response_data = response.json()
                return response_data
            else:
                print(f'Request failed. Expected 200, got {response.status_code}: {response.text}')
                return None
        except requests.exceptions.Timeout as e:
            print(f'API request timed out: {e}')
            continue
        except requests.exceptions.RequestException as e:
            print(f'An error occurred during the request: {e}')
            return None
    
    print('Failed to access API.')
    return None