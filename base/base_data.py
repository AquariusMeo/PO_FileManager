import yaml


def get_data(file_name, key):
    with open("./data/" + file_name + ".yml", 'r', encoding='utf-8') as f:
        return yaml.load(f)[key].values()
