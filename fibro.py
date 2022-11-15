def fiboNacci(x):
    n1,n2 = 0,1 # es lo mismo que n1=0/n2=1
    nth=n1+n2
    print(n1)
    print(n2)
    count=2
    while count<x:
        print(nth)
        n1=n2
        n2=nth
        nth=n1+n2
        count=count+1

fiboNacci(13)
