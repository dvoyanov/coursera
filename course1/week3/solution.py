
class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name) as f:
                return f.read()
        except FileNotFoundError:
            return ''



if __name__ == "__main__":
    test_file_reader = FileReader("/etc/passwd")
    print(test_file_reader.read())

