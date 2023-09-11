
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_number=max(arr)
    print(max_number)
    l=[]
    runner=0
    big=max_number
    
    for i in range(n):
        if( arr[i]<big ):
            l.append(arr[i])
    
    print(max(l))
            