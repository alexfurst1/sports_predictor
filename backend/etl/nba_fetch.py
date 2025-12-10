from balldontlie import BalldontlieAPI
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

BALLDONTLIE_KEY = os.getenv("BALLDONTLIE_KEY")
api = BalldontlieAPI(api_key=BALLDONTLIE_KEY)

headers = {
            "Authorization" : BALLDONTLIE_KEY
        }

#year = int(datetime.today().strftime("%Y"))
#seasons_to_fetch = [year,year-1,year-2]

def fetch_season(season: int, per_page: int = 100):
    all_games = [] # 
    base_url = f'https://api.balldontlie.io/v1/games'
    cursor = None

    while True:

        params = {
            "seasons[]" : season,
            "per_page" : per_page
        }
        if cursor:
            params["cursor"] = cursor

        r = requests.get(base_url,headers=headers,params=params)
            
        if r.status_code == 200:
            print("Sucess!")
        else:
            print(f"Error: {r.status_code}")

        try:
            data = r.json()
            games_list = data["data"]

            for game_dict in games_list:
                all_games.append(game_dict)            

            if cursor:
                print(f"successfully appended batch with cursor {params["cursor"]}")
            else:
                print("Printed first batch successfully!")
        except Exception as e:
            print(f"Error: {e}")

        cursor = data["meta"].get("next_cursor")
        if not cursor:
            break
        elif r.status_code == 429:
            print("Too many requests, waiting 1 minute before fetching next batch...")
            time.sleep(61) # this is because balldontlie API only allows 5 requests/min currently.
            print("61 seconds have passed, gathering next batch.")

    return all_games
    
"""
games = fetch_season(2024)

i = 1
for print_game in games:
    print(print_game)
    print(f"game {i}")
    i += 1
    """
