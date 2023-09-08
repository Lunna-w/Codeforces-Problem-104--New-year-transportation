n, t = list(map(int, input().split()))
path = list(map(int, input().split()))

position = 1  

while position < t:  
    position += path[position - 1]  

if position == t:
    print("YES")
else:
    print("NO")

