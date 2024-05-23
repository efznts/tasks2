import csv


def get_averages(file_path):
    with open(file_path, 'r+') as file:
        reader = csv.reader(file)
        columns = None
        sums = []
        counts = []

        for row in reader:
            if columns is None:
                columns = len(row)
                sums = [0.0] * columns
                counts = [0] * columns

            for i in range(columns):
                value = float(row[i])
                sums[i] += value
                counts[i] += 1

        averages = [sums[i] / counts[i] if counts[i] != 0 else 0 for i in range(columns)]
        return averages


def print_averages(averages):
    for i, avg in enumerate(averages):
        print(avg)
