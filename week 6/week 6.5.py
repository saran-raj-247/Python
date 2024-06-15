def zip_lists(list1, list2):
    # Zip the lists and concatenate corresponding sublists
    zipped_list = [sublist1 + sublist2 for sublist1, sublist2 in zip(list1, list2)]
    return zipped_list

m = int(input())
n = int(input())
list1 = [[int(input()) for _ in range(n)] for _ in range(m)]
list2 = [[int(input()) for _ in range(n)] for _ in range(m)]
zipped_list = zip_lists(list1, list2)
print(zipped_list)
