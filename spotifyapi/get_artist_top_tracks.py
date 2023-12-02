from spotifyapi.query_spotify_api import query_spotify
from spotifyapi.api_constants import ARTISTS_ENDPOINT

def get_artist_top_tracks(artist_id:str, access_token:str, market='US') -> list or None:
    """Retrieve top tracks for an artist from the Spotify API.

    Tiven an artist ID, this function will query the Spotify API for the artist's top tracks. 
    If the request is successful, it will return the list of top tracks. If the request times out,
    it will print an error and return None. If the request fails, it will print an error and return None.

    Args:
        artist_id: A Spotify artist ID.
        access_token: A valid access token from the Spotify API.
        market: An ISO 3166-1 alpha-2 country code for which the top tracks are determined.

    Returns:
        A list of top tracks for the specified artist.

    Raises:
        TimeoutError: If the request times out.
        RequestException: If the request fails (the status code is not 200).

    Example:
        >>> artist_id = '4PTG3Z6ehGkBFwjybzWkR8'
        >>> access_token = get_access_token(client_id, client_secret, timeout=60, retries=3)
        >>> top_tracks = get_artist_top_tracks(artist_id, access_token, market='US)
    """
        
    ## Define artist data endpoint
    endpoint = f'{ARTISTS_ENDPOINT}/{artist_id}/top-tracks?market={market}'
    print(endpoint)
    print('Getting track data...')

    track_data = query_spotify(endpoint, access_token=access_token)
    return track_data