import yaml

def get_full_fake(path:str):

    with open(path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return data
