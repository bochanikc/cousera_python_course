import json
import argparse
import os
import tempfile


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', required=True)
    parser.add_argument('--value')
    parser.add_argument('--clear')

    return parser


def get_parametrs(parser):
    namespace = parser.parse_args()
    key = namespace.key
    value = namespace.value
    clear = namespace.clear
    return key, value, clear


def get_file():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    return storage_path


def write_file(data):
    storage_path = get_file()
    with open(storage_path, 'w') as f:
        f.write(data)


def read_file():
    storage_path = get_file()
    with open(storage_path, 'r') as f:
        data = f.read()
        if data != "":
            data = json.loads(data)
        else:
            data = {}
        return data

def clear_file():
    storage_path = get_file()
    with open(storage_path, 'w') as f:
        f.close()


def write_key_value(key, value):
    try:
        data = read_file()
    except FileNotFoundError:
        data = {}
    if key in data:
        data[key] = data[key] + ", " + value
    else:
        data[key] = value
    data = json.dumps(data)
    write_file(data)


def get_value_with_key(key):
    try:
        data = read_file()
    except FileNotFoundError:
        return None

    if key in data:
        value = data[key]
        return value
    else:
        return None


if __name__ == '__main__':
    parser = create_parser()
    key, value, clear = get_parametrs(parser)

    if value is None:
        print(get_value_with_key(key))
    elif clear is not None:
        clear_file()
    else:
        write_key_value(key, value)
