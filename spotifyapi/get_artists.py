from spotifyapi.query_spotify_api import query_spotify
from spotifyapi.api_constants import ARTISTS_ENDPOINT
from typing import Union

def get_artists(artist_ids: Union[str, list[str]], access_token: str):

    """
    Retrieve artist data for one or multiple artists from the Spotify API.

    Args:
        artist_ids (str or list): A single artist ID as a string or a list of artist IDs.
        access_token (str): Spotify access token for authentication.

    Returns:
        dict: Artist data for the specified artist(s).

    Example:
        >>> artist_ids = '0TnOYISbd1XYRBk9myaseg'
        >>> access_token = 'your_spotify_access_token'
        >>> artist_info = get_artists(artist_ids, access_token)
    """

    ## Define artist data endpoint
    # Changes if querying one or multiple artists 
    endpoint = (f'{ARTISTS_ENDPOINT}/{artist_ids}' if isinstance(artist_ids, str) 
                else f'{ARTISTS_ENDPOINT}?ids={",".join(artist_ids)}')

    print(endpoint)
    print('Getting artists data...')

    artist_data = query_spotify(endpoint, access_token=access_token)    
    return artist_data