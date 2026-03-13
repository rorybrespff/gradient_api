# GradientPy
GradientPy is a Python library developed by Gradient Sports (https://www.gradientsports.com) to provide a convenient way to access the Gradient Sport REST API from applications written in Python.


### Step 1 - Clone this repo
Use the below code to clone this repo onto your local environment

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


### Step 3 - Retrive data 
To retreive the data

* Set up as functions that are downloaded
* Set up as clone that will run off a separate script
* Discuss how each of the functions will operate
    * load_api_token()
    * get_gameList()
    * get_gameEvents_game()
    * get_gaemEvents_gameList()
    * filter_by_gameEventType()

### Notes
Run main.py

This includes selecting variables for:
* Competition_name: Select the competitions you require for your analysis (this will be limited based on your API access)
* Season: Select the seasons you require for your analysis (this will be limited based on your API access)
* eventType: Allows you to select specific event types (i.e. Passes, Shots etc) or all for your analysis
