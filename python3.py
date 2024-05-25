import requests
import json
import sqlite3

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    
    return response.json()

def store_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def print_launch_info(data):
    if data:
        name = data['name']
        date = data['date_utc']
        details = data.get('details', 'No details available')
        
        print(f"Launch Name: {name}")
        print(f"Launch Date: {date}")
        print(f"Details: {details}")
    else:
        print("No data to display.")

def store_in_database(data):
    if data:
        conn = sqlite3.connect('spacex_launches.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Launches
                     (id TEXT PRIMARY KEY, name TEXT, date TEXT, details TEXT)''')
        
        id = data['id']
        name = data['name']
        date = data['date_utc']
        details = data.get('details', 'No details available')
        
        c.execute("INSERT OR IGNORE INTO Launches (id, name, date, details) VALUES (?, ?, ?, ?)", 
                  (id, name, date, details))
        conn.commit()
        conn.close()
    else:
        print("No data to store in database.")

if __name__ == "__main__":
    data = fetch_spacex_launches()
    
    if data:
        store_json(data, 'spacex_launch.json')
        
        print_launch_info(data)
        
        store_in_database(data)
