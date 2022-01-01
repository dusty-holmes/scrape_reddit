# Scrape_Reddit
`scrape_reddit` is a console application that downloads data from Reddit.  The data is downloaded to the screen or JSON file.

This tool is intended to be called via bash script and scheduled with cron
to help build datasets from reddit.

The tool can be ran without installing using:

`$python main.py`

## Installation

Install with `pip install -e . `

then call the tool using:
`scrape_reddit -h`

which returns:

```
usage: scrape_reddit [-h] [--subreddit [SUBREDDIT]]
                     [--search [{hot,rising,new,controversial,top}]]
                     [--filter [{all,day,hour,month,week,year}]]
                     [--limit [LIMIT]] [--filename [FILENAME]]

This console application scrapes submissions from reddit. Authentication is
handled by setting environment variables. Results are printed to screen or
saved to file in a JSON format.

optional arguments:
  -h, --help            show this help message and exit
  --subreddit [SUBREDDIT]
                        The subreddit to search. Subreddits can be combined
                        with a '+' symbol.
  --search [{hot,rising,new,controversial,top}]
                        The type of search function to use.
  --filter [{all,day,hour,month,week,year}]
                        The timeframe of the top search.
  --limit [LIMIT]       Number of rows to return from the search.
  --filename [FILENAME]
                        The filename to save JSON file output as. If not
                        provided, results will be printed to screen.
```