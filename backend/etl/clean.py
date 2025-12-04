def clean_game(raw_dict):
    if raw_dict["status"] != "Final":
        return None
    
