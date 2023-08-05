import os, json

class Config:
    
    def __init__(self, route):
        self.route = route

        self.snippets_dir = './data/snippets.json'

    def read_data(self):
        with open(self.snippets_dir, "r") as file:
            data = json.load(file)
        return data

    def save_data(self, data):
        with open(self.snippets_dir, "w") as file:
            json.dump(data, file)
