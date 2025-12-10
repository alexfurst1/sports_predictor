# function that takes a game dict from nba_fetch.py, and slims it down to only the fields I need. also checks for missing values and such

# fields needed: game_date, season, home_score_id, away_score_id, home_score, away_score, winner_team_id

import nba_fetch


def clean_game(game_dict):
    