import re as r

if(input("test?\n") in ["1", "t", "y"]):
    n = open("input_test.txt", "r")
else:
    n = open("input.txt", "r")

d = {"r": 12, "g": 13, "b": 14}
s = 0
S = 0

for l in n:
    v = True
    l = r.split(",|;|:", l.strip().replace("reen", "").replace("ed", "").replace("lue", "").replace("Game ", "").replace(" ", ""))
    
    # p1
    for c in l:
        if("b" in c or "r" in c or "g" in c):
            if(int(c[:-1]) > d[c[-1]]):
                v = False
            
    if(v):
        s += int(l[0])
    
    # p2
    R = max([int(c[:-1]) for c in l if c[-1] == "r"])
    G = max([int(c[:-1]) for c in l if c[-1] == "g"])
    B = max([int(c[:-1]) for c in l if c[-1] == "b"])
    S += R * G * B
print(s)
print(S)
    
    