T = int(input())
for x in range(1, T + 1):
    n=int(input())
    inp = sorted(list(map(int,list(input().split(" ")))))
    m=0
    for i in inp:
        if (m+1)<=i:
            m+=1
    print("Case #{}: {}".format(x,m), flush=True)
