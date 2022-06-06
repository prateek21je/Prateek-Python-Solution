# Q6
def prime(a, b):
    list = []
    for i in range(a, b):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                list.append(i)
    return list

starting = int(input("starting: "))
ending = int(input("ending: "))
pme = prime(starting, ending)
if len(pme) == 0:
    print("no prime numbers ")
else:
    print("prime numbers in this range : ", pme)