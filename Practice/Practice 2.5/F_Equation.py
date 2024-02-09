def calcu(x,n):
    sum=0
    powr_x=0
    for i in range(0,n+1,2):
        sum+=x**i
        powr_x+=1
    return sum

x,n=map(int,input.split())
res=calcu(x,n)
print(res-1)
