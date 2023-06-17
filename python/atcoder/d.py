n=int(input())
a=list(map(int,input().split()))
b=[]
b.append(a[0])
print(len(b))
for i in range(1,n):
    if len(b)==0:
        b.append(a[i])
        print(len(b))
    else:
        if a[i-1]==a[i] and a[i]!=a[i+1]:
            ok=True
            count=0
            while ok:
                del[i]
                
            del b[-1]
            print(len(b))
        else:
            b.append(a[i])
            print(len(b))

    