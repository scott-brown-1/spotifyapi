from spotifyapi.query_spotify_api import query_spotify
from spotifyapi.api_constants import AUDIO_FEATURES_ENDPOINT

def get_tracks_audio_features(track_ids: Union[str, List[str]], access_token: str):

    """
    Retrieve audio features for one or multiple tracks from the Spotify API.

    Args:
        track_ids (str or list): A single track ID as a string or a list of track IDs.
        access_token (str): Spotify access token for authentication.

    Returns:
        dict: Audio features data for the specified track(s).

    Example:
        >>> track_ids = '4cOdK2wGLETKBW3PvgPWqT'
        >>> access_token = 'your_spotify_access_token'
        >>> audio_features = get_tracks_audio_features(track_ids, access_token)
    """
    
    # Define audio feature endpoint
    endpoint = (f'{AUDIO_FEATURES_ENDPOINT}/{track_ids}' if isinstance(track_ids, str) 
                else f'{AUDIO_FEATURES_ENDPOINT}?ids={",".join(track_ids)}')

    print(endpoint)
    print('Getting audio feature data...')

    audio_data = query_spotify(endpoint, access_token=access_token)    
    return audio_data


    ## Define audio feature endpoint
    # Changes if querying one or multiple tracks 
    endpoint = (f'{AUDIO_FEATURES_ENDPOINT}/{track_ids}' if isinstance(track_ids, str) 
                else f'{AUDIO_FEATURES_ENDPOINT}?ids={",".join(track_ids)}')

    print(endpoint)
    print('Getting audio feature data...')

    audio_data = query_spotify(endpoint, access_token=access_token)    
    return audio_data