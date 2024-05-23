import csv


def sum_column(file, column_name):
    total_sum = 0

    with open(file, 'r+') as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_sum += int(row[column_name])

    return total_sum
