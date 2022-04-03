T = int(input())
for x in range(1, T + 1):
    p1 = list(map(int,list(input().split(" "))))
    p2 = list(map(int, list(input().split(" "))))
    p3 = list(map(int, list(input().split(" "))))
    minc = min(p1[0],p2[0],p3[0])
    minm = min(p1[1], p2[1], p3[1])
    miny = min(p1[2], p2[2], p3[2])
    mink = min(p1[3], p2[3], p3[3])
    minreq= 1000000
    sumin=minc+minm +miny+mink
    l=[minc,minm,miny,mink]
    if sumin<minreq:
        print("Case #{}: {}".format(x, "IMPOSSIBLE"), flush=True)
    if sumin ==minreq:
        print("Case #{}: {} {} {} {}".format(x,minc,minm,miny,mink), flush=True)
    if sumin >minreq:
        diff=sumin-minreq
        for i in range(4):
            if diff<l[i]:
                l[i]-=diff
                diff=0
                sumin = sum(l)
                if sumin == minreq:
                    print("Case #{}: {} {} {} {}".format(x,l[0],l[1],l[2],l[3]), flush=True)
                    break
            else:
                diff=diff-l[i]
                l[i]=0
                sumin=sum(l)
