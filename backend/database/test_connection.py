from supabase_client import supabase

def main():
    result = supabase.table("teams").select("*").limit(1).execute()
    print(result)


if __name__ == "__main__":
    main()

# if you get the data array that means it working, regardless if its empty or not