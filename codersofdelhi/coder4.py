import json
def load_data(filename):
    with open(filename,"r") as f:
        return json.load(f)
# functions to find pages a user might like based on common interests
def find_pages_you_might_like(user_id,data):
    # dictionary to store user interactions with pages
    user_pages={}
    # populate the dictionary
    for user in data['users']:
        user_pages[user['id']]=set(user['liked_pages'])
    # if the user is not found ,return an empty list 
    if user_id not in user_pages:
        return []
    user_liked_pages=user_pages[user_id]
    page_suggestion={}
    for other_user, pages in user_pages.items():
        if other_user!=user_id:
            shared_pages=user_liked_pages.intersection(pages)
        for page in pages:
            if page not in user_liked_pages:
                page_suggestion[page]=page_suggestion.get(page,0) +len(shared_pages)

    sorted_pages=sorted(page_suggestion.items(),key=lambda x:x[1],reverse=True) 
    return [(page_id,score) for page_id,score in sorted_pages]   
data=load_data("codersofdelhi/data3.json") 
user_id=1
page_recommended=find_pages_you_might_like(user_id,data)
print(page_recommended)       
    
