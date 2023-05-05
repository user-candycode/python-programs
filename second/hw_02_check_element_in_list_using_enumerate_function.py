l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(l):
    index += 1
    if index == 3 or index == 5 or index == 7:
        print(item)
