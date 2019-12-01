#Generate Rhythm Exercise
import numpy as np

beats = 4
sub = 2 
nhitsmin = 2

nhits = np.random.choice(range(nhitsmin, beats*sub))
rhythm = np.random.choice(range(beats*sub), nhits, replace=False)

out = '||'
for r in range(beats*sub):
    if r in rhythm:
        out += 'x'
    else:
        out += '-'
    if r%sub == sub-1:
        out += '|'
out += '|'        

print(out)
