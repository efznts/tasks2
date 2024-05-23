import re
from collections import Counter


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_words(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words


def count_words(words):
    return Counter(words)


def most_common_words(word_counts):
    most_common = word_counts.most_common()
    for word, count in most_common:
        print(word, ':', count)


file_path = './file.txt'
text = read_file(file_path)
words = get_words(text)
word_counts = count_words(words)
most_common_words(word_counts)
