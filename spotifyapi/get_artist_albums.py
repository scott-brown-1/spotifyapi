from spotifyapi.query_spotify_api import query_spotify
from spotifyapi.api_constants import ARTISTS_ENDPOINT

def get_artist_albums(artist_id:str, access_token:str, limit:int=10):
    """Retrieve a list of an artist's albums and the albums' data for a given artist ID.

    Given an artist ID and an access token, this function will query the Spotify API for a list of the artist's albums 
    and the albums' data. If the request is successful, it will return the response data. If the request fails, it will
    print an error and return None. If the request is successful, but the status code is not 200, it will print an error and return None.

    Args:
        artist_id: A Spotify artist ID.
        access_token: A valid access token from the Spotify API.
        limit: The maximum number of albums to return.

    Returns:
        A list of album data from the Spotify API.

    Raises:
        TimeoutError: If the request times out.
        RequestException: If the request fails (the status code is not 200).

    Example:
        >>> artist_id = '4PTG3Z6ehGkBFwjybzWkR8'
        >>> access_token = get_access_token(client_id, client_secret, timeout=60, retries=3)
        >>> album_data = get_artist_albums(artist_id, access_token, limit=10)
    """
    ## Define artist data endpoint
    endpoint = f'{ARTISTS_ENDPOINT}{artist_id}/albums?limit={limit}'
    print('Getting album data...')

    album_data = query_spotify(endpoint, access_token=access_token)
    return album_data