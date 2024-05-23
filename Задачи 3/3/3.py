import csv


def read_file(filename, column):
    values = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = float(row[column])
            values.append(value)

    min_value = min(values)
    max_value = max(values)

    print('Минимальное значение в столбце:', min_value)
    print('Максимальное значение в столбце:', max_value)


read_file('./weather.csv', 'temp_max')
