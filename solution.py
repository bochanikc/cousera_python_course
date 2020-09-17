class FileReader:

    def __init__(self, path):
        self.path = path

    def read(self):
        data = ''
        try:
            with open(self.path, 'r') as file:
                data = file.read()
        except FileNotFoundError as e:
            data = ''
        return data
