def merge(start, mid, end, l, temp):
    inv = 0
    i = start 
    j = mid + 1
    k = start
    
    while(i<= mid  and j <= end):
        if l[i] <= l[j]:
            temp[k] = l[i]
            i += 1
            k += 1
        else:
            temp[k] = l[j]
            j += 1
            k += 1
            inv += (mid - i + 1)
            
    while(i <= mid ):
        temp[k] = l[i]
        k += 1
        i += 1
        
    while(j <= end):
        temp[k] = l[j]
        j += 1
        k += 1
        
    for i in range(start, end + 1):
        l[i] = temp[i]
        
    return inv

def merge_sort_helper(start, end, l, temp):
    
    inv = 0
    
    if start < end:  
        mid = (end + start)//2
        inv += merge_sort_helper(start, mid, l, temp)
        inv += merge_sort_helper(mid + 1, end, l, temp)
        inv += merge(start, mid, end, l, temp)
        
    return inv
        
def merge_sort(l,n):
    start = 0
    end = n - 1
    temp = [0] * n
    return merge_sort_helper(start, end, l, temp)

t = int(input())
for i in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    print(merge_sort(l,n))
