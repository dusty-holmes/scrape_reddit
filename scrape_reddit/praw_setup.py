import praw
import os
import importlib.resources
import json
from typing import List
from dotenv import load_dotenv

# Alias for passing parameters to below functions
field_list = List[str]
flat_json = List[dict]

# List of all environment variables to load up
with importlib.resources.open_text("scrape_reddit", "settings.json") as file:
    settings =  json.load(file)

# field names saved in .env file to authenticate with PRAW 
env_fields = settings['env_fields']

# List of fields to retrieve for every submission
submission_fields = settings['submission_fields']

# The timeframe of a top() search
time_choices = settings['time_choices']

# The type of search to execute
search_choices = settings["search_choices"]

def get_reddit():
    """
    Load credentials from .env file and use to load PRAW object
    """
    load_dotenv()
    reddit_credentials = {field : os.environ.get(field) for field in env_fields }
    return praw.Reddit(**reddit_credentials)

def submission_search( subreddit : str = 'all',
                   search : search_choices = 'top',
                   filter : time_choices = 'hour',
                   limit : int = 100,
                   reddit : object = get_reddit(),
                   submission_fields : field_list = submission_fields
            ) -> flat_json:
    """
    Returns a list of dictionaries containing submission data from a subreddit
    """
    rows=[]
    search_args = { 'limit': limit }

    # top search has additional time_filter
    if search == 'top':
        submission_search = reddit.subreddit(subreddit).top
        search_args['time_filter'] = filter
    else:
        submission_search = getattr(reddit.subreddit(subreddit), search)

    for submission in submission_search(**search_args):
        row={}
        [row.update({field:getattr(submission, field)}) for field in submission_fields]
        row['subreddit'] = submission.subreddit.display_name
        rows.append(row)
        
    return rows