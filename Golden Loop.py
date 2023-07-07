def print_positive_numbers(list1):
    result = []
    for num in list1:
        if num >= 0:
            result.append(num)
    return result

list1 = [12, -7, 5, 64, -14]
print(f"Output: {print_positive_numbers(list1)}")

list2 = [12, 14, -95, 3]
print(f"Output: {print_positive_numbers(list2)}")
