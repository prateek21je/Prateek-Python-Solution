Q1


x = int(input("enter numbers "))

y = input("asc, desc, none: ")
res = [int(x) for x in str(x)]
if y == "asc":
    res.sort()
print(str(res))
if y == "desc":
    res.sort(reverse=True)
print(str(res))
if y == "none":
    print(str(res))


