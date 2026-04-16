import json

def search_json_file(file_path, query):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        query = query.strip().lower()
        results = []

        for item in data:
            # City, Address ebong Name er moddhe query khujbe
            city = str(item.get('city', '')).lower()
            address = str(item.get('address', '')).lower()
            name = str(item.get('name', '')).lower()

            if query in city or query in address or query in name:
                results.append(item)

        if results:
            print(f"\n--- {len(results)} ti Result Pauya Geche ---")
            for i, res in enumerate(results, 1):
                print(f"{i}. Name: {res['name']}")
                print(f"   Address: {res['address']}")
                print(f"   Phone: {res['phone1']}")
                print("-" * 30)
        else:
            print("Kono result pauya jayni.")

    except Exception as e:
        print(f"Error: {e}")

# Use it like this:
file_name = 'ContactData.json'
search_term = input("Search Location (e.g., Dhaka, Gazipur, Shantinagar): ")
search_json_file(file_name, search_term)