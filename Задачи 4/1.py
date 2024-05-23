from itertools import permutations


def generate_combinations(word):
    all_combinations = set([''.join(p) for p in permutations(word)])
    return all_combinations


combinations = generate_combinations('qwerty')
for combination in combinations:
    print(combination)
