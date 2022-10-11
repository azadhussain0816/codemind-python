for t in range(int(input())):
    n = int(input())
    np = n
    nb = n
    while True:
        fc =0 

        for i in range(1,np+1):
            if np%i==0:
                fc+=1
        if fc==2:
            break
        np+=1
    while True: 
        fb = 0
        for i in range(nb,0,-1):
            if nb%i==0:
                fb+=1
        if fb == 2:
            break
        nb-=1
    if n-nb<=np-n:
        print(nb)
    else:
        print(np)