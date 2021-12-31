from setuptools import setup
setup(
    name='scrape_reddit',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'scrape_reddit=scrape_reddit.main:run'
        ]
    }
)