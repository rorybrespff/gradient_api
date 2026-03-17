import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import time
#from gradient_api import load_api_token, get_gameList, get_gameEvents_game, get_gameEvents_gameList, filter_gameEventType
from functions import (load_api_token, get_gameList, get_gameEvents_game, get_gameEvents_gameList, filter_gameEventType)

header = load_api_token()

season = ['2025-2026']
competition_name = ['Premier League']

game_id_list = get_gameList(competition_name, season, header)
game_id_list = game_id_list[0:9]

df = get_gameEvents_gameList(game_id_list, header=header)
df = filter_gameEventType(df, gameEventType_list=['CR'])