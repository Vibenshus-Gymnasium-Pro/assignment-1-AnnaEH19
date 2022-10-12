all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
special1_numbers = [1]
special2_numbers = [2]
special3_numbers = [3]

for all_numbers in all_numbers:
    if all_numbers in special1_numbers:
        print(all_numbers, "st")
    elif all_numbers in special2_numbers:
        print(all_numbers, "nd")
    elif all_numbers in special3_numbers:
        print(all_numbers, "rd")
    else:
        print(all_numbers, "th")