import requests
import pandas as pd
#import numpy as np
import os
from dotenv import load_dotenv
import time


## AUTHORIZATION FUNCTIONS

def load_api_token():
    
    # Load environment
    load_dotenv()

    # Get your API token
    bearer_token = os.getenv("API_TOKEN")

    # Create authorisation header
    header = {"Authorization": f"Bearer {bearer_token}"}
    
    return header


## GAME FUNCTIONS

def get_gameList(competition_name=None, season=None, header=None):
    
    # Flag if user has not provided their API token
    if header is None:
        print('No API Token provided. Please ensure your Gradient API token is saved in your .env file and called used the load_api_token() function.')
    
    # Calculate time at start of request
    start_time = time.time()
    
    # Create response
    url = "https://interia.gradientsports.com/api/v1/games"
    response = requests.get(url, headers=header)
    
    # Flag errors
    response.raise_for_status()
    print("Game List Status: ", response.status_code)
    
    # Access data
    games_json = response.json()
    games_data = games_json["data"]
    games_df = pd.json_normalize(games_data['games'])
    
    # Filter for season/competition (if lists are provided)
    if competition_name:
        games_df = games_df.loc[games_df['competition.name'].isin(competition_name)]
    if season:
        games_df = games_df.loc[games_df['season'].isin(season)]
    
    # Convert Game IDs to list
    game_id_list = games_df.id.to_list()
    
    # Calculate time at end of request and print time it took handle this request
    end_time = time.time()
    print(f"Game List Processing Time: {end_time - start_time:.2f} seconds")
    
    return game_id_list



## GAME EVENTS FUNCTIONS

def get_gameEvents_game(game_id, header=None):
    
    # Calculate time at start of request
    start_time = time.time()
    
    # Response
    try:
        # Flag if user has not provided their API token
        if header is None:
            print('No API Token provided. Please ensure your Gradient API token is saved in your .env file and called used the load_api_token() function.')
        # Create response if API token is provided
        else:
            url = f"https://interia.gradientsports.com/api/v1/games/{game_id}/events"
            response = requests.get(url, headers=header)
            response.raise_for_status()
            print(f"Game {game_id} Status: {response.status_code}")
    # Add exception if an error is encountered with this game. This will not provide data for this game but will allow to skip to next game (if part of a processing loop).
    except requests.exceptions.HTTPError as e:
        print(f"Skipping game {game_id}: {e}")
        return None
    
    # Access data
    events_json = response.json()
    gameEvents = events_json['data']['gameEvents']
    ge_df = pd.DataFrame(gameEvents)
    
    # Calculate time at end of request and print time it took handle this request
    end_time = time.time()
    print(f"Game {game_id} Processing Time: {end_time - start_time:.2f} seconds")
    
    return ge_df

def get_gameEvents_gameList(game_list, header=None, delay=3, chunk_size=30, chunk_pause=300):
    
    # Create initial empty list to append dataframes into as soon as they are requested and processed
    df_list = []
    
    # Loop through games in game list
    for i, game_id in enumerate(game_list):
        
        # Get data for individual game
        dfg = get_gameEvents_game(game_id, header)
        # Append data to list
        df_list.append(dfg)
        # Add delay to prevent queuing
        time.sleep(delay)
        
        # Add logic to pause processing (default 300 seconds) after 30 games to avoid queuing
        if (i + 1) % chunk_size == 0:
            print(f"Processed {i+1} games, pausing {chunk_pause}s...")
            time.sleep(chunk_pause)
    
    # Once processing of all games is complete, concat them into one single dataframe
    df = pd.concat(df_list, ignore_index=True)
    
    return df


## GAME EVENT FILTERING

def filter_gameEventType(dataframe, gameEventType_list=[]):
    
    # Flag to user to include game event types in list in order to filter data
    if gameEventType_list==[]:
        print('Please list Game Event Types you would like to filter by and resubmit function')
    else:
        # Filter data by game event types provided
        df_filtered = dataframe.loc[dataframe['eventType'].isin(gameEventType_list)].reset_index(drop=True)
        # Return empty dataframe if those game events are not available in dataframe provided
        if df_filtered.empty:
            return None
        # Create dataframe that expands dictionary in 'details' column
        df_details = pd.json_normalize(df_filtered['details'])
        # Merge this 'details' dataframe onto the original dataframe
        df_final = pd.concat([df_filtered, df_details], axis=1)
        
        return df_final
