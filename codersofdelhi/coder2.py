# load the data
import json
def clean_data(data):
    # remove users with missing name
    data['users']=[user for user in data['users'] if user["name"].strip()]
    # remove duplicate friends
    for user in data['users']:
        user['friends']=list(set(user['friends']))
    # remove inactive users    
    data['users']=[user for user in data['users'] if user['friends'] or user['liked_pages']]
    # remove duplicate pages
    unique_pages={}
    for page in data['pages']:
        unique_pages[page['id']]=page
    data['pages']=list(unique_pages.values())    
    return data



data = json.load(open("codersofdelhi/data2.json"))
data=clean_data(data)
json.dump(data,open("codersofdelhi/cleaned_data2.json","w"), indent=4)
print("data has been cleaned successfully")