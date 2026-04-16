arr=list(map(int,input().split()))
n=len(arr)
stack=[]
ans=[]
for i in range(0,n):
    while(len(stack)!=0 and stack[-1]<=arr[i]):
        stack.pop()
    if(len(stack)==0):
        ans.append(-1)
    else:
        ans.append(stack[-1])
    stack.append(arr[i])
print(ans)
    


