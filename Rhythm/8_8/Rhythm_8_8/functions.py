import numpy as np



# Group
def group(seq):
    res = []
    
    if len(set(seq)) == 1:
        res.append(seq[0]*8)
    
    else:
        div = [seq[:4], seq[4:]]
        for d in range(len(div)):
            if len(set(div[d])) == 1:
                div[d] = div[d][0]*4
                res.append(div[d][0]*4)
            else:
                div2 = [div[d][:2], div[d][2:]]
                for d2 in range(len(div2)):
                    if len(set(div2[d2])) == 1:
                        div2[d2] = div2[d2][0]*2
                        res.append(div2[d2][0]*2)
                    else:
                        res.append(div2[d2][0])
                        res.append(div2[d2][1])                    
                div[d] = div2
                
    return (res)





#
#x = ['1', '1', '1', '1', '0', '1', '1', '1']
#
#
#for i in range(10):
#    x = list(np.random.choice(['0','1'], 8))
#    print(x)
#    grouped = (group(x))
#    print(grouped)
#    print()


