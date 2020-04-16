import json
import ast

def load_db():
    with open("country.json") as f:
        return json.load(f)

def load_2():
    with open("alldetails.json") as d:
        return json.load(d)


def from_html_to_json(list):
    with open("alldetails.json", "w") as json_file:
        json.dump(list, json_file)

def save_db(data):
    with open("country.json", "w") as write_file:
        json.dump(data, write_file) 

def add_key_to_dict(country,patients,current):
     with open("country.json") as data_flie:
        data = json.load(data_flie)
        for sub in data:
            if sub['country'] == country:  
                number_of_curent_patients = int(patients) + current
                print(number_of_curent_patients)
                sub['total'] = int(patients) + int(sub['total'])
                sub['patients'] = patients
                print(sub['total'])   
                return sub['total']       
        # print(data)
        # save_db(data)

def number_in_json(country):
     with open("country.json") as data_flie:
        data = json.load(data_flie)
        counter = 0
        for sub in data:
            counter += 1
            if sub['country'] == country:  
                return counter
       

def number_of_curent_patients(country):
 with open("country.json") as data_flie:
        data = json.load(data_flie)
        for sub in data:
            if sub['country'] == country:
                return int(sub['patients'])

def returnjson(text):
    print(type(text))
    res = json.loads(text)
    return(res)

def check_if_alredy_exist(country):
    print(country)
    with open("country.json","r") as data_flie:
        data = json.load(data_flie)
        # if data.get(country) != None:
        # if 'country' in data:
        for sub in data:
            print(sub['country'])
            if sub['country'] == country:
                return 1
        else:
            return 0      

db = load_db()
rb = load_2()