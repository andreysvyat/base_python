from os import path as file_info


def print_descriptor(path: str):
    print(file_info.abspath(path),
          file_info.getsize(path),
          file_info.getmtime(path),
          sep='\n')
