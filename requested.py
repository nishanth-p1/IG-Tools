# Run this file in the same folder you have your pending_follow_requests.json as
# the output will be all the instagram pages you are still requested to follow

import json

# Open correct file
with open('pending_follow_requests.json') as file:
    requested_json = json.load(file)

# Make array list of requested accounts
requested_list = []
for user in requested_json["relationships_follow_requests_sent"]:
    requested_list.append(user["string_list_data"][0]["value"])

# Print out requested accounts
for user in requested_list:
    print(user)