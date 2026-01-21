import json
# lets write a function to load the data
def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
    return data    
data=load_data("codersofdelhi/data1.json")
print(data)
print(type(data))

# write a function to display users and their connections

def display_users(data):
    print("Users and their connections\n")
    for user in data['users']:
        print(f"ID:{user['id']} - {user['name']} is friends with: {user['friends']} and liked pages are {user['liked_pages']} ")
    print("pages information")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']} ")
print(display_users(data))     

   