import os
import tempfile
import uuid


class File:

    def __init__(self, path_to_file):
        self.counter = 0
        self.path_to_file = path_to_file

        try:
            f = open(path_to_file)
            f.close()
        except FileNotFoundError:
            with open(path_to_file, 'tw') as f:
                pass

    def __str__(self):
        return os.path.abspath(self.path_to_file)

    def __iter__(self):
        self.data = self.read()
        return self

    def __next__(self):
        with open(self.path_to_file, 'r') as f:
            f.seek(self.counter)

            line = f.readline()
            if not line:
                self.counter = 0
                raise StopIteration

            self.counter = f.tell()

            return line

    def read(self):
        with open(self.path_to_file, 'r') as f:
            return f.read()

    def write(self, string):
        self.limit = len(string)

        with open(self.path_to_file, 'w') as f:
            f.write(string)
            return len(string)

    def __add__(self, other):
        text1 = self.read()
        text2 = other.read()

        text = text1 + text2
        new_file = File(os.path.join(tempfile.gettempdir(), uuid.uuid4().hex))
        new_file.write(text)
        return new_file


# file_obj = File('example.txt')
# file_obj.write('line 1\nline 2\nline 3\n')
# lines = iter(file_obj)
# print(len(list[lines]))
# print()
# for line in file_obj:
#     #print(len(list[file_obj]))
#     print(ascii(line))

