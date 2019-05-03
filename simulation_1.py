from random import randint

def simulation(t):
    n = 0
    c = 0
    for x in range (0,t):
        t1 = randint(1,6)
        t2 = randint(1,6)
        if t1 + t2 == 7:
            #print ("term:",x,":",t1 + t2)
            c = c + 1
            if c > 4:
                n = n + 1
        else:
            #print ("term",x,":",t1 + t2)
            c = 0
    return n

print ("average time of 5 consecutive 7 in 10000 rows is:")
r = 0
for temp in range (0,100):
    r = r + simulation(10000)
res = r/100
print (res)
print ("possibility is: ",res/10000)
#print (simulation(10000))