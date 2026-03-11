import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from functions import *

header = load_api_token()

season = ['2025-2026']
competition_name = ['Premier League']

game_id_list = get_game_list(competition_name, season, header)
df = get_gameEvents_for_game_list(game_id_list, eventType=['CR'])