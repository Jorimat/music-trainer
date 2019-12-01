with open('patterns.txt', 'r') as f:
    lines = f.readlines()
    
pattern2 = []
pat = ''
for line in lines:
    pat += line
    if line.rstrip(' \n')[-1] == ';':
        pattern2.append(pat.rstrip(';'))
        pat = ''