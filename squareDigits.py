def add_numbers_in_binary(num1: int, num2: int) -> str:
    """Adds two numbers and returns their sum in binary format without using bin()."""
    total = num1 + num2
    binary_result = ""

    if total == 0:
        return "0"

    while total > 0:
        binary_result = str(total % 2) + binary_result
        total //= 2

    return binary_result


# Example usage:
result = [add_numbers_in_binary(5, 3), add_numbers_in_binary(12, 28)]
print(result)  # Output: 1000
