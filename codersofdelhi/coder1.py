import json
def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
    return data    
data=load_data("codersofdelhi/data1.json")
print(data)
print(type(data))
