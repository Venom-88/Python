my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):
    element = my_list[index]
    if element < 0:
        break
    elif element == 0:
        index += 1
        continue
    else:
        print(element)
    index += 1