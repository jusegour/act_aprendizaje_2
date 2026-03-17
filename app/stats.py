def mean(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)


def max_value(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


def min_value(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return min(numbers)