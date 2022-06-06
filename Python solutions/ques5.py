#Q6

import array
array=[]
def fcn(array):
    for i in range(0, len(array)):    
        for j in range(i+1, len(array)):    
            if(array[i] > array[j]):    
                temp = array[i]  
                array[i] = array[j]    
                array[j] = temp  
    for j in range(100):
        if array[j]==array[j+1]:
            print(array[j])
fcn([1,2,3,4,5,6,5,])
