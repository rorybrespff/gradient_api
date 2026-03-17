# Import packages
import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import time
from datetime import datetime
#from gradient_api import load_api_token, get_gameList, get_gameEvents_game, get_gameEvents_gameList, filter_gameEventType
from functions import (load_api_token, get_gameList, get_gameEvents_game, get_gameEvents_gameList, filter_gameEventType)


# Load authorisation header
header = load_api_token()

# Set filter variables
season = ['2025-2026']
competition_name = ['Premier League']
gameEventTypes = ['CR']

# Retrive game list
game_id_list = get_gameList(competition_name, season, header)

# Create Game Events dataframe for games in game list
df = get_gameEvents_gameList(game_id_list, header=header)

# Filter by game event types
df = filter_gameEventType(df, gameEventType_list=gameEventTypes)

# Set today's date
date=datetime.today().strftime('%Y%m%d')

# Export dataframe to CSV
df.to_csv(f'exports/gameEventDataframe_{date}.csv')