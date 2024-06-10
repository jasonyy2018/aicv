import json
import os

config_file_path = 'config.json'

def load_config():
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as config_file:
            return json.load(config_file)
    return {}

def save_config(config_data):
    with open(config_file_path, 'w') as config_file:
        json.dump(config_data, config_file)