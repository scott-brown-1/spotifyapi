"""
Module storing constants for the Spotify API.

.. data:: DATA_DIR

    Path to directory to store saved access token 

.. data:: ARTISTS_ENDPOINT

    Get Spotify catalog information for a single artist identified by their unique Spotify ID.

.. data:: AUDIO_FEATURES_ENDPOINT

    Get audio feature information for a single track identified by its unique Spotify ID.
"""

## Path to directory to store saved access token
DATA_DIR = './spotifyapi/data'

## Spotify API endpoints
ARTISTS_ENDPOINT = 'https://api.spotify.com/v1/artists' # get info about an artist
AUDIO_FEATURES_ENDPOINT = 'https://api.spotify.com/v1/audio-features' # get audio features from a song