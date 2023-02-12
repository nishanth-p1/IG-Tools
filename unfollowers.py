# Run this file in the same folder you have your followers.json and following.json files as
# the output will be all the instagram pages aren't following you back

import json

# Open correct files
with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

# Make array list of accounts not following back
unfollower_list = []
for following in following_json["relationships_following"]:
    unfollower_list.append(following["string_list_data"][0]["value"])

for follower in followers_json["relationships_followers"]:
    if follower["string_list_data"][0]["value"] in unfollower_list:
        unfollower_list.remove(follower["string_list_data"][0]["value"])

# Print out accounts not following back
for user in unfollower_list:
    print(user)