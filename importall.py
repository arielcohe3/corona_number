import json

def load_2():
    with open("alldetails.json") as f:
        return json.load(f)


def from_html_to_json(list):
    with open("alldetails.json", "w") as json_file:
        json.dump(list, json_file)

      

rb = load_2()