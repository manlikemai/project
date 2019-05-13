num = int(input("Enter number:"))
lst = [0,1]
if num == 1:
    print(lst[0])

elif num == 2:
    print(lst)

elif num > 2:
    for i in range(2,num):
        a = lst[len(lst)-1] + lst[len(lst)-2]
        lst.append(a)
    print(lst)

else:
    print("invalid input")
