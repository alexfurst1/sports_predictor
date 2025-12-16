# ----- Runs the full ETL pipeline.

from backend.etl import nba_fetch, clean, load
from datetime import datetime

def run_pipeline():
    data = []
    cleaned_data = []
    year = int(datetime.today().strftime("%Y"))
    seasons = [year,year-1,year-2]

    for season in seasons:
        data.extend(nba_fetch.fetch_season(season))

    for game in data:
        cleaned_data.append(clean.clean_game(game))

    if load.load_teams(data):
        print("loaded teams to supabase in pipeline")
        if load.load_games(cleaned_data):
            print("loaded games to supabase in pipeline")
    else:
        print("load error in pipeline")

if __name__ == "__main__":
    run_pipeline()
