# GradientPy
GradientPy is a Python library developed by Gradient Sports (https://www.gradientsports.com) to provide a convenient way to access the Gradient Sport REST API from applications written in Python.


## Set Up


### Step 1 - Install this package
Use the below code to install our repo onto your local environment

```
pip install git+https://github.com/rorybrespff/gradient_api.git 
```


### Step 2 - Set up your environment
To access data via the Gradient API, you will require an API token. 

If you do not currently have an API token, please contact support@gradientsports.com and we will look to set up you up with a token with appropriate access.

Once you have an API token, please save this to an .env file in the parent directory of this repo. This should be saved in the below format:

```
API_TOKEN="{YOUR_API_TOKEN}"
```


### Step 3 - Access data 

#### Load your API token
To access your API token from your environment, you can use this function:

```
load_api_token()
```

This will return your Authorisation header to access the Gradient REST API.

#### List of Game IDs
To create a list of the game IDs for specific competition(s), you can use this function:

```
get_gameList(competition_name=None, season=None, header=None)
```

This requires you to provide:
* **competition_name**: A list of the competition names you want to include (i.e. ["Premier League", "La Liga"])
* **season**: A list of the season(s) you want to include (i.e. ["2024-2025"])
* **header**: Your API token that you will need to retrieve using the load_api_token() function

The data is returned as a list.

#### Game Events (inc. Location Data) for one game
To retrieve game event data for one game, you can use this function

```
get_gameEvents_game(game_id, header=None)
```

This requires you to provide:
* **game_id**: The game ID for the specfic game (i.e. 31995)
* **header**: Your API token that you will need to retrieve using the load_api_token() function

The data is returned as a pandas Dataframe.

#### Game Events (inc. Location Data) for list of games
To retrieve game event data for a list of games, you can use this function

```
get_gameEvents_gameList(game_list, header=None, delay=3, chunk_size=30, chunk_pause=300)
```

This requires you to provide:
* **game_list**: A list of game IDs (i.e. [31995,31996,31997,31998,31999,32000]). You can generate a list of game IDs for a specfic competition(s) and season(s) using the get_GameList() funcition.
* **header**: Your API token that you will need to retrieve using the load_api_token() function.
* **delay**: Pause time (in seconds) between requests for game data. This stops immediately requesting new games that can create processing backlog. Default of 3 seconds is appropriate for most requests.
* **chunk_size**: The number of games you want to process before pausing requests. This allows game backlog time to process in large volume request. Default of 30 games is appropriate for most requests.
* **chunk_pause**: Pause time (in seconds) between game chunks being processed. This allows game backlog time to process in large volume request. Default of 300 seconds is appropriate for most requests.

The data is returned as a pandas Dataframe.

#### Filter Game Events by Game Event Type
Once you have retrieved the Game Event data, you can filter the data by the type of game event(s) using this function:

```
filter_gameEventType(dataframe, gameEventType_list=[])
```

This requires you to provide:
* **dataframe**: Game Event data retrieved using either the get_GameEvents_game() or get_GameEvents_gameList().
* **gameEventType_list**: List of the game events (i.e. ["CR", "PA"])

This returns a pandas Dataframe.

### Step 4 - Run a script
We have a provided a sample script cross_data.py that will return data for cross event data for the 2024-2025 Premier League season (access permitting). 


## Questions and Support
Our hope is that the above provides you with the information you need to begin exploring our Gradient REST API. However, if you have any questions or run into issues, please reach out to us at support@gradientsports.com
