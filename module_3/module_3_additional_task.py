def calculate_structure_sum(data):
    total = 0
    if isinstance(data, dict):
        elements = list(data.keys()) + list(data.values())
    elif isinstance(data, (list, tuple, set)):
        elements = data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, (int, float)):
        return data
    else:
        return 0

    for item in elements:
        total += calculate_structure_sum(item)
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
