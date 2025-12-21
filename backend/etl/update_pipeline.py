# ----- Runs the full ETL pipeline.

from backend.etl import nba_fetch, clean, load
from datetime import datetime

def run_pipeline():
    raw_data = []
    cleaned_data = []
    year = int(datetime.today().strftime("%Y"))
    seasons = [year,year-1,year-2]

    for season in seasons:
        raw_data.extend(nba_fetch.fetch_season(season))

    for game in raw_data:
        cleaned_game = clean.clean_game(game)
        if cleaned_game is not None:
            cleaned_data.append(cleaned_game)

    if load.load_teams(raw_data):
        print("loaded teams to supabase in pipeline")
        if load.load_games(cleaned_data):
            print("loaded games to supabase in pipeline")
        else:
            print("error with loading games")
    else:
        print("load error in pipeline")

if __name__ == "__main__":
    run_pipeline()
