

import requests
import json


'''
TASK 2 : Connect to this API endpoint http://api.football-data.org/v4/competitions/ 
Extract all the competition names into a separate list

'''

# API endpoint to fetch football competitions
url = 'http://api.football-data.org/v4/competitions/'


# Send request to the API
football = requests.get(url)

# Parse API response as JSON
compete = football.json()


# Extract competitions list
Result = compete['competitions']

# Initialize list to store competition names
competiton_names = []
for outcome in Result:
    football_names = outcome['name']
    competiton_names.append(football_names)
# Print competition names
print("Competiton name:" ,competiton_names)    