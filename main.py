import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import time
#from gradient_api import load_api_token, get_game_list, get_gameEvents_for_game_list

from functions import (
    load_api_token,
    get_gameList,
    get_gameEvents_game,
    get_gameEvents_gameList,
    filter_gameEventType
)

header = load_api_token()

season = ['2025-2026']
competition_name = ['Premier League']

game_id_list = get_gameList(competition_name, season, header)
game_id_list = game_id_list[0:9]

df = get_gameEvents_gameList(game_id_list, header=header)
df = filter_gameEventType(df, gameEventType_list=['CR'])


#df = get_gameEvents_for_game_list(game_id_list, eventType=['CR'], header=header, base_delay=1)
#df = get_gameEvents_for_game_list(game_list_test, eventType=['CR'], header=header)

#test = get_gameEvents_for_game(40899, eventType=['CR'], header=header)

# def rate_limited_fetch(game_id, eventType=None, header=None, delay=1):
#     time.sleep(delay)  # Delay before each request
#     return get_gameEvents_for_game(game_id, eventType=eventType, header=header)

# with ThreadPoolExecutor(max_workers=2) as executor:
#     get_cross_events = partial(rate_limited_fetch, eventType=['CR'], header=header, delay=1)
#     results = list(executor.map(get_cross_events, game_list_test))
    
# df_cross = pd.concat([r for r in results if r is not None and not r.empty], ignore_index=True)