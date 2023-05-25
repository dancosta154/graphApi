import json
import sys

def loadJson(file):
    with open(file) as f:
        data = json.load(f)
    return data

def activityOverview(file):

    jsonData = loadJson(file)

    posts = jsonData['data']['influencer']['instagram']['medias']
    
    post_list = {}
    
    for i in range(len(posts)):
        root = jsonData['data']['influencer']['instagram']['medias'][i]

        post = i +1 
        username = root['username']
        id = root['id']
        timeStamp = root['timestamp']
        likeCount = root['like_count']
        mediaType = root['media_type']
        # Use get() method with a default value
        caption = root.get('caption', '')  

        # Check if the username exists in the dictionary
        if username not in post_list:
            post_list[username] = []

        # Append the values to the list under the username key
        post_list[username].append({
            'PostNo': post,
            'PostId': id,
            'TimeStamp': timeStamp,
            'LikesCount': likeCount,
            'MediaType': mediaType,
            'Caption': caption
        })
    
    return post_list

def mediaOverview(file):
    
    jsonData = loadJson(file)

    media = jsonData['data']['influencer']['instagram']['medias']

    media_list = []
    for i in range(len(media)):

        engagement = media[i]['data'][0]
        impressions = media[i]['data'][1]
        reach = media[i]['data'][2]

        Id = engagement['id'].split("/")[0]

        engagement_activity = f"ENGAGEMENT: {Id} - {engagement['description']}: {engagement['values'][0]['value']}"
        impressions_activity = f"IMPRESSION: {impressions['description']}: {impressions['values'][0]['value']}"
        reach_activity = f"REACH: {reach['description']}: {reach['values'][0]['value']}"

        media_list.append(engagement_activity)
        media_list.append(impressions_activity)
        media_list.append(reach_activity)
        media_list.append('----*****----')

    return media_list

if __name__ == "__main__":
    file = sys.argv[1]
    print(mediaOverview(file))
