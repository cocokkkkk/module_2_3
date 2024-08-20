my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
cnt = 0

while cnt < len(my_list):
    if my_list[cnt] < 0:
        break
    elif my_list[cnt] > 0:
        print(my_list[cnt])
    cnt += 1



