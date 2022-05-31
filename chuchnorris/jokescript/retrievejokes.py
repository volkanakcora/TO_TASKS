import requests
import json 
from . import CollectorBase
import pandas as pd 
import os

print(os.getcwd())

class jokes(CollectorBase):
    def run(self):
        chuck_morris = requests.get('https://api.chucknorris.io/jokes/random')
        json_data = json.loads(chuck_morris.text)
        with open("jokes.txt", "w") as myfile:
            myfile.write(json_data['value'])
        return json_data['value']