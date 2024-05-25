
## Project Description
This project fetches the latest SpaceX launch data from the SpaceX API and performs the following tasks:
1. Uses the `requests` module to fetch the data and demonstrates the use of several attributes/functions such as `get()`, `status_code`, and `headers`.
2. Stores the fetched JSON data into a file named `spacex_launch.json`.
3. Extracts and prints specific information from the JSON data, including the launch name, date, and details.
4. Stores the extracted information into an SQLite database called `spacex_launches.db`.
## Requirements

- `requests`
- `json`
- `sqlite3`
