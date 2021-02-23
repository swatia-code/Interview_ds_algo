class Solution:

    def count(self,arr, n, x):
        # code here
        def first_occurence(l: list, n: int, x: int) -> int:
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
            
        if first_occurence(arr, n, x) == -1:
            return 0
        else:
            return last_occurence(arr, n, x)  - first_occurence(arr, n, x) + 1


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1
