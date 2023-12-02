import os
import yaml

def parse_yaml_config(filename, env=None):
    env = env or os.getenv('DEVENV', 'docker')
    env_dict = {'docker': 0, 'local': 1}
    env_index = env_dict.get(env, 0)

    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    def parsing_array_element(data):
        if isinstance(data, dict):
            for key, value in data.items():
                data[key] = parsing_array_element(value)
        elif isinstance(data, list):
            data = parsing_array_element(data[env_index]) if data else None
        return data

    return parsing_array_element(data)