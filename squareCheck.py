def is_square(n):
    if n < 0:
        return False
    root = 0
    while root * root <= n:
        if root * root == n:
            print(root * root, root)
            return True
        root += 1
    return False


test_data = [-1, 0, 3, 4, 25, 26]
for i in test_data:
    print(f'{i} is a square number: {is_square(i)}')
