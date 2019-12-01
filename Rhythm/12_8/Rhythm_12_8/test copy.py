

import numpy as np



# Python code to flat a nested list with 
# multiple levels of nesting allowed. 
#  
# input list 
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] 
  
# output list 
#output = [] 
  
flattened = []    
# function used for removing nested  
# lists in python.  
def reemovNestings(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            flattened.append(i)
            
## Driver code 
#print ('The original list: ', l) 
#reemovNestings(l) 
#print ('The list after removing nesting: ', output) 






def nest(x):
    # Base case: '0'
    if len(x) in [2,3]:
        return x

    # Recursive case: '0...'
    else:
        sublen=int(len(x)/2)
        return [nest(x[:sublen]), nest(x[sublen:])]
    
    
def isnested(l):
    return np.any([type(item) == list for item in l])
    

def group(l):
    if len(set(l)) == 1:
        return (''.join(l))
    else:
        return(l)

    
def flatten(l):
    return list(np.array(l).flatten())


    
seq = list(np.random.choice(['0','1'], 12))
print(seq)
nested = nest(seq)
print(nested)


res = []
def group(l):
    for sub in l:
        flattened = flatten(sub)
        if len(set(flattened)) == 1:
            res.append(''.join(flattened))
        elif type(sub) == list:
            group(sub)
group(nested)
          
    
print(res)






#output = []
#def regroup(l):
#    flattened = []
#    reemovNestings(l)
#    
#    if len(set(flattened)) == 1:
#        print(''.join(flattened))
#        
#    else:
#        for item in l:
#            regroup(item)
#
#regroup(nested)









#output = [] 
#def reemovNestings(l): 
#    for i in l: 
#        if isnested(i):
#            reemovNestings(i) 
#        else:
#            output.append(group(i))
#
#reemovNestings(nested) 
#print (output) 




#seq = list(np.random.choice(['0','1'], 12))
#print(seq)
#nested = nest(seq)
#print(nested)
#print()
#
#
#seq = list(np.random.choice(['0','1'], 16))
#print(seq)
#nested = nest(seq)
#print(nested)
#print()