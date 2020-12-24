import os
import tempfile

class File:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, 'w') as f:
                pass

    def read(self):
        with open(self.path_to_file) as f:
            return f.read()

    def write(self, string):
        with open(self.path_to_file, 'w') as f:
            return f.write(string)

    def __add__(self, file_object):
        with tempfile.NamedTemporaryFile() as f:
            path_to_new_file = f.name
        new_file =  File(path_to_new_file)
        new_file.write(self.read()+file_object.read())
        return new_file

    def __iter__(self):
        with open(self.path_to_file) as f:
            self.iter_list_file = f.readlines()
            self.current = 0
        return self

    def __next__(self):
        if self.current >= len(self.iter_list_file):
            raise StopIteration

        self.current += 1
        return self.iter_list_file[self.current - 1]

    def __str__(self):
        return os.path.abspath(self.path_to_file)
    
