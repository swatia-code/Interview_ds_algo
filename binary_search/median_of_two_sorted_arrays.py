class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        X = nums1 if len(nums1) <= len(nums2) else nums2
        Y = nums2 if len(nums2) >= len(nums1) else nums1
        
        x = len(X)
        y = len(Y)
        
        low = 0
        high = x
        
        while low <= high:
            part_x = (low+high)//2
            part_y = (x + y + 1)//2 - part_x
            
            max_x_left = X[part_x-1] if part_x != 0 else -sys.maxsize
            max_y_left = Y[part_y-1] if part_y != 0 else -sys.maxsize
            
            min_x_right = X[part_x] if part_x != x else sys.maxsize
            min_y_right = Y[part_y] if part_y != y else sys.maxsize
            
            if min_x_right >= max_y_left and min_y_right >= max_x_left:
                return max(max_x_left, max_y_left) if (x+y) % 2 else (max(max_x_left, max_y_left) + min(min_y_right, min_x_right))/2
            elif max_y_left < min_x_right:
                high = part_x - 1
            else:
                low = part_x + 1
