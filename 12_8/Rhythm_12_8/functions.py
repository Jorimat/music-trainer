import numpy as np


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


#
#
#def regroup(l):
#    for sub in l:
#        flattened = flatten(sub)
#        if len(set(flattened)) == 1:
#            res.append(''.join(flattened))
#        elif type(sub) == list:
#            regroup(sub)