
def print_file_descriptor(path: str):
    print(open(path, 'rb').fileno())
