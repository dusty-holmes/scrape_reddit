import argparse
from .praw_setup import search_choices, time_choices

def get_parser():
    parser = argparse.ArgumentParser( 
        description = """
This console application scrapes submissions from reddit.  Authentication is 
handled by setting environment variables.  Results are printed to screen or
saved to file in a JSON format.
        """)

    parser.add_argument(
        '--subreddit',
        type=str,
        nargs='?',
        const='all',
        default='all',
        help="The subreddit to search.  Subreddits can be combined with a '+' symbol."
    )

    parser.add_argument(
        '--search',
        choices=search_choices+['top'],
        type=str,
        nargs='?',
        const='top',
        default='top',
        help="The type of search function to use."
    )

    parser.add_argument(
        '--filter',
        choices=time_choices,
        type=str,
        nargs='?',
        const="hour",
        default="hour",
        help="The timeframe of the top search."
    )

    parser.add_argument(
        '--limit',
        type=int,
        nargs='?',
        const=100,
        default=100,
        help="Number of rows to return from the search."
    )

    parser.add_argument(
        '--filename',
        type=str,
        nargs='?',
        help="The filename to save JSON file output as. " + 
             "If not provided, results will be printed to screen."
    )

    return parser.parse_args()