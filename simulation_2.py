from random import randint

def simulation(t):
    n = 0
    c = 0
    for x in range (0,t):
        t1 = randint(1,6)
        t2 = randint(1,6)
        if t1 + t2 == 7:
            #print (t1 + t2)
            n = n + 1
        else:
            #print (t1 + t2)
            c = c + 1
    return c/n

print ("average number before 7 occur is:")
print (simulation(10000))