# Program to perform CRUD on json file
import json
with open('car.json','r') as f:
    data = json.load(f)
# CRUD operations
#Read  
for car in data['state']:
    print(car)

#create
with open('new_car.json','w') as f:
    json.dump(data,f, indent=2)

    
#Update
demo = {'name':"Kartik",'age':"22"}
with open("new_car.json","r+") as json_update_file:
    json.dump(demo, json_update_file)
    
    
# Delete
with open('car.json','w') as extra_data:
    for element in data:
        if 'x' in element:
            'x'.clear()
    print(car)