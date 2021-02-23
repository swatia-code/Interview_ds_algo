#code
def first_occurence(l: list, n: int, x: int) -> int:
    """
    param: l: sorted list
    param: n: size of list
    param: x: key whose first index has to be found
    return first occurence index
    """
    start, end = 0, n - 1
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if l[mid] == x:
            res = mid
            end = mid - 1
        elif l[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
            
    return res
    
def last_occurence(l: list, n: int, x: int) -> int:
    """
    param: l: sorted list
    param: n: size of list
    param: x: key whose last index has to be found
    return last occurence index
    """
    start, end = 0, n - 1
    res = -1
    while start <= end:
        mid = start + (end - start) // 2
        if l[mid] == x:
            res = mid
            start = mid + 1
        elif l[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
            
    return res
    

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    l = [int(x) for x in input().split()]
    if first_occurence(l, n, x) == -1:
        print(-1)
    else:
        print(first_occurence(l, n, x), last_occurence(l, n, x))
