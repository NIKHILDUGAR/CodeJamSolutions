T = int(input())
for x in range(1, T + 1):
    inp = list(input().split(" "))
    r,c=int(inp[0]),int(inp[1])
    s="""..+-+
..|.|
+-+-+
|.|.|
+-+-+"""
    l=s.splitlines()
    r=r-2
    c=c-2
    if c > 0:
        for _ in range(c):
            l[0]+='-+'
            l[1]+='.|'
            l[2]+='-+'
            l[3]+='.|'
            l[4] += '-+'
    if r>0:
        for _ in range(r):
            l.append(l[-2])
            l.append(l[-2])
    print("Case #{}:".format(x), flush=True)
    for i in l:
        print(i)
