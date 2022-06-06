# Q7
def fction(a,x):
    count=0
    for i in a:
        if i==x:count+=1
    return count

a=[2,3,5,2,5,2,2,5]
x=2
print(fction(a,x))