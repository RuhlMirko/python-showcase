def is_square(n):
    if n >= 0:
        result = (n**0.5) % 1 == 0
    else:
        return False
    return result


test_data = [-1, 0, 3, 4, 25, 26]
for i in test_data:
    print(f'{i} is a square number: {is_square(i)}')
