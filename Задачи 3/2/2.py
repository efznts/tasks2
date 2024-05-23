import csv

with open("data.csv", "w+") as file1:
    writer = csv.writer(file1)
    writer.writerows([
        ["Имя", "Фамилия", "Возраст"],
        ["Дмитрий", "Иванов", 25],
        ["Алексей", "Петров", 30]])


def read_file(filename):
    with open(filename) as file2:
        reader = csv.reader(file2)
        for row in reader:
            print(row)


read_file('./data.csv')
