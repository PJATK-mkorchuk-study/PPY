lst = [3, 78, 34, 123, 17, 19, 23, 76, 89]
my_dict = {}
temp_lst = []
r = int(input("Enter an integer: "))
for i in range(1, r):
    temp_lst = []
    for j in range(0, len(lst)):
        if (lst[j] % r == i):
            temp_lst.append(lst[j])
        my_dict.update({str(i): temp_lst})

print(my_dict)
