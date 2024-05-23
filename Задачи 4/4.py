def longest_sequence(arr):
    n = len(arr)
    if n == 0:
        return []

    lengths = [1] * n
    predecessors = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] >= arr[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j

    max_length_index = 0
    for i in range(1, n):
        if lengths[i] > lengths[max_length_index]:
            max_length_index = i

    sequence = []
    k = max_length_index
    while k != -1:
        sequence.append(arr[k])
        k = predecessors[k]

    sequence.reverse()
    return sequence


arr = [5, 3, 4, 4, 2, 1, 2, 3, 4, 1]
result = longest_sequence(arr)
print(result)
