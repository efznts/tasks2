def read_file(file):
    with open(file, 'r+') as file:
        result = file.read()
        print(result)


read_file('./example.txt')
