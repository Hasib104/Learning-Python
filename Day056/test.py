
def remove_all_before(items, border):
    for i in range(len(items)):

        if items[i] == border:
            print(items[i:])

remove_all_before([1, 2, 3, 4, 5], 3)
remove_all_before([1, 1, 2, 2, 3, 3], 2)
remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)
remove_all_before([1, 1, 5, 6, 7], 2)
remove_all_before([], 0)
remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)