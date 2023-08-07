import json
from components import TagDataclass

class Config:
    
    def __init__(self, route):
        self.route = route

        self.snippets_dir = './data/snippets.json'
        self.tags_dir = './data/tags.json'

    def read_snippets_data(self):
        with open(self.snippets_dir, "r") as file:
            data = json.load(file)
        return data

    def save_snippets_data(self, data):
        with open(self.snippets_dir, "w") as file:
            json.dump(data, file)

    def read_tags_data(self):
        with open(self.tags_dir, "r") as file:
            data = json.load(file)

        tags = [TagDataclass(id = tag['id'], color = tag['color'], text = tag['text']) for tag in data]
        
        return tags
    
    def save_tags_data(self, tag):
        with open(self.tags_dir, "r+") as file:
            file_data = json.load(file)
            file.seek(0)
            data = {
                'id': tag.id,
                'color': tag.color,
                'text': tag.text
            }

            file_data.append(data)
            json.dump(file_data, file)
