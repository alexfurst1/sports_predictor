# function that takes a game dict from nba_fetch.py, and slims it down to only the fields I need. also checks for missing values and such
# only cleans finished games, and regular season games. playoffs games will be included in the future.


import nba_fetch


def clean_game(game_dict):
    new_dict = {}

    if game_dict["status"] == "Final" and game_dict["postseason"] == False: 
        try:
                game_date = str(game_dict["date"])
                season = int(game_dict["season"])
                home_team_id = int(game_dict["home_team"]["id"])
                away_team_id = int(game_dict["visitor_team"]["id"])
                home_score = int(game_dict["home_team_score"])
                away_score = int(game_dict["visitor_team_score"])
                #historically no NBA game has never ended in a tie, so I don't include a feature to track it.
                if home_score > away_score:
                    winner_team_id = home_team_id
                else:
                    winner_team_id = away_team_id
        except Exception as e:
            print(f"Error in clean_game in clean.py: {e}")

    new_dict["game_date"] = game_date
    new_dict["season"] = season
    new_dict["home_team_id"] = home_team_id
    new_dict["away_team_id"] = away_team_id
    new_dict["home_score"] = home_score
    new_dict["away_score"] = away_score
    new_dict["winner_team_id"] = winner_team_id

    return new_dict

        