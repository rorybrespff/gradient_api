import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv


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

def get_game_list(competition_name=None, season=None, header=None):
    
    # Flag if user has not 
    if header==None:
        print('No Authorization Header provided. Please provide in function to access data')
    
    # Create response
    url = "https://interia.gradientsports.com/api/v1/games"
    response = requests.get(url, headers=header)
    
    # Flag errors
    response.raise_for_status()
    print("Status: ", response.status_code)
    
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
    
    return game_id_list



## GAME EVENTS FUNCTIONS

def get_gameEvents_for_game(game_id, eventType=None, header=None):
    
    # Response
    try:
        url = f"https://interia.gradientsports.com/api/v1/games/{game_id}/events"
        response = requests.get(url, headers=header)
        response.raise_for_status()
        print(f"Game {game_id} Status: {response.status_code}")
    except requests.exceptions.HTTPError as e:
        print(f"Skipping game {game_id}: {e}")
        return None
        
    # Access data
    events_json = response.json()
    gameEvents = events_json['data']['gameEvents']
    
    # Create dataframe 
    if eventType==None:
        df_final = pd.json_normalize(gameEvents)
    elif eventType!=None:
        df_ge = pd.DataFrame(gameEvents)
        df_et = df_ge.loc[df_ge['eventType'].isin(eventType)].reset_index(drop=True)
        if df_et.empty:
            None
        df_details = pd.json_normalize(df_et['details'])
        df_final = pd.concat([df_et, df_details], axis=1)
    
    return df_final


def get_gameEvents_for_game_list(game_id_list, eventType=None):
    
    df_list = []
    
    for game_id in game_id_list:
        dfg = get_gameEvents_for_game(game_id, eventType)
        df_list.append(dfg)
        
    df = pd.concat(df_list)
    
    return df