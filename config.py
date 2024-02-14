import json
from components import TagDataclass

class Config:
    
    def __init__(self, route):
        self.route = route

        self.snippets_dir = './data/snippets.json'
        self.tags_dir = './data/tags.json'
        self.users_dir = './data/users.json'

    def read_snippets_data(self, id = None):
        with open(self.snippets_dir, "r") as file:
            data = json.load(file)

        if id:
            data = next((snip for snip in data if snip['id'] == id), None)
        return data

    def save_snippets_data(self, data):
        with open(self.snippets_dir, "w") as file:
            json.dump(data, file, indent=2)

    def read_tags_data(self):
        with open(self.tags_dir, "r") as file:
            data = json.load(file)

        tags = [TagDataclass(id = tag['id'], text = tag['text']) for tag in data]
        
        return tags
    
    def save_tags_data(self, tag):
        with open(self.tags_dir, "r+") as file:
            file_data = json.load(file)
            file.seek(0)
            data = {
                'id': tag.id,
                'text': tag.text
            }

            file_data.append(data)
            json.dump(file_data, file)

    def get_user_data(self, username):
        with open(self.users_dir, "r") as file:
            data = json.load(file)

        data = next((user for user in data if user['username'] == username), None)
        return data
    
    def save_user_data(self, user):
        with open(self.users_dir, "r+") as file:
            file_data = json.load(file)
            file.seek(0)
            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'password': user.password
            }
            file_data.append(data)
            json.dump(file_data, file)
