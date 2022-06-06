# Q8
# (eg. S = “h20 15 wa73r”, so sum will be 2+0+1+5+7+3).

def findsum(str1):
    temp="0"
    sum=0

    for ch in str1:
        if(ch.isdigit()):
            temp += ch
        else:
            sum += int(temp)
            temp = "0"
    return sum + int(temp)

str1="45t7bhjvba9ca"
print(findsum(str1))