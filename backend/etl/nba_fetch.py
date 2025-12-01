from balldontlie import BalldontlieAPI
from dotenv import load_dotenv
import os
import datetime
import requests

load_dotenv()

BALLDONTLIE_KEY = os.getenv("BALLDONTLIE_KEY")

api = BalldontlieAPI(api_key="BALLDONTLIE_KEY")

# fetch games for the current season up until yesterday, and then all games 3 seasons prior

def get_games():
    today = datetime.now().year()
    seasons = [today,today-1,today-2]
    all_games = []

    for season in seasons:
        for game in api.nba.games.list(season=season, per_page=100):
            all_games.append(game.dict())




