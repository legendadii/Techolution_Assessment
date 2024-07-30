import json
import os

class UserStorage:
    def __init__(self, filename):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)  # Initialize with an empty list

    def load_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_entry(self, entry):
        data = self.load_data()
        data.append(entry)
        self.save_data(data)

    def get_entries(self):
        return self.load_data()

    def find_entry(self, key, value):
        data = self.load_data()
        return [entry for entry in data if entry.get(key) == value]
