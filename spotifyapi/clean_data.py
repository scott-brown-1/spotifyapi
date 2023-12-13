import pandas as pd

def join_tables(track_arg, artist_arg, audio_feature_arg, use_dfs=True):
    """
    Join three tables based on common columns.

    Parameters:
    - track_arg (str or DataFrame): File path or DataFrame for the track data.
    - artist_arg (str or DataFrame): File path or DataFrame for the artist data.
    - audio_feature_arg (str or DataFrame): File path or DataFrame for the audio feature data.
    - use_dfs (bool, optional): If True, treat the arguments as DataFrame objects.
                                If False, treat the arguments as file paths and read them using pandas.
                                Default is True.

    Returns:
    - DataFrame: Merged data.

    Example:
    >>> result_df_objects = spotifyapi.join_tables(track_df, artist_df, audio_feature_df, use_dfs=True)
    """

    # Load the CSV files or use the provided DataFrames
    track_df = track_arg if use_dfs else pd.read_csv(track_arg)
    artist_df = artist_arg if use_dfs else pd.read_csv(artist_arg)
    audio_feature_df = audio_feature_arg if use_dfs else pd.read_csv(audio_feature_arg)

    # Merge track_df with artist_df based on 'artist_id'
    merged_data = pd.merge(track_df, artist_df, on='artist_id')

    # Merge the result with audio_feature_df based on 'track_id'
    final_merged_data = pd.merge(merged_data, audio_feature_df, on='track_id')

    return final_merged_data

def clean_genres(df, prioritized_genres):
    """
    Filter the 'genres' column of a DataFrame to keep only prioritized genres or genres containing the listed genres
    Order Matters, if there is Indie Rock, and the list is ('Indie', 'Pop', 'Rock'), 'Indie' will be kept.

    Parameters:
    - df (DataFrame): Input DataFrame.
    - prioritized_genres (list): List of prioritized genres.

    Returns:
    - DataFrame: Filtered DataFrame with only prioritized genres.
    """
    filtered_df = df.copy()  # Create a copy to avoid modifying the original DataFrame
    
    # Convert 'genres' column from string to list
    filtered_df['genres'] = filtered_df['genres'].apply(lambda x: eval(x) if pd.notnull(x) else [])
    
    # Loop through each list item in the 'genres' column and replace genres
    for i in range(len(filtered_df['genres'])):
        for j in range(len(filtered_df['genres'][i])):
            for prioritized_genre in prioritized_genres:
                # Check if the current genre contains a prioritized genre word
                if prioritized_genre.lower() in filtered_df['genres'][i][j].lower():
                    filtered_df['genres'][i][j] = prioritized_genre
                    break  # Stop searching for matches once found

    return filtered_df