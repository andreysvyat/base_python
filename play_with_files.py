file_name = 'C:\\Users\\andre\\OneDrive\\Documents\\Rockstar Games\\GTA V\\settings.xml'

fb = open(file_name, 'rb')
f = open(file_name, 'r')


def print_tells():
    print(fb.tell())
    print(f.tell())


def read(c: int):
    print(fb.read(c))
    print(f.read(c))


def seek(offset: int, whence: int):
    fb.seek(offset, whence)
    f.seek(offset, 0)


print_tells()
read(10)
print_tells()
seek(12, 2)
print_tells()
print(*fb.readlines(), sep='\n')
print(*f.readlines(), sep='\n')
