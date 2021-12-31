import json
from pprint import pprint
from .arg_parser import get_parser
from .praw_setup import submission_search

def run():
    parser = get_parser()
    submissions = submission_search(
        subreddit= parser.subreddit,
        search= parser.search,
        filter= parser.filter,
        limit=parser.limit)

    if parser.filename:
        with open(parser.filename, 'w') as json_file:
            json.dump(submissions, json_file)
    else:
        pprint(submissions)

if __name__ == '__main__':
    run()