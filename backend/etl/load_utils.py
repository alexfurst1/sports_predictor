from backend.database.supabase_client import supabase

def batch_upsert(
        table_name: str,
        rows: list[dict],
        conflict_column : str,
        batch_size: int = 100
):
    if not rows:
        print("rows data parameter is missing")
        return
    
    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]

        supabase.table(table_name).upsert(batch, on_conflict=conflict_column).execute()
