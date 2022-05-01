# https://practice.geeksforgeeks.org/problems/quick-sort/1/#
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pivot_index = self.partition(arr,low,high)
            self.quickSort(arr,low,pivot_index-1) 
            self.quickSort(arr,pivot_index+1, high)
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high]
        pivot_index = high
        while low < high: 
            if arr[low] < pivot:
                low += 1
                continue
            else:
                if arr[high] >= pivot:
                    high -= 1
                    continue
                else:
                    arr[low], arr[high] = arr[high], arr[low]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return high

obj = Solution()
arr = [4,1,3,9,7]
obj.quickSort(arr,0,len(arr)-1)
print(arr)



# https://algo.monster/problems/sorting_intro
def sort_list(unsorted_list: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    def quickSort(arr, low, high):
        if low >= high:
            return
        pivot_index = high
        ori_low = low
        while low < high:
            if arr[low] < arr[pivot_index]:
                low += 1
                
            else:
                if arr[high] >= arr[pivot_index]:
                    high -= 1
                    
                else:
                    arr[low], arr[high] = arr[high], arr[low]
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        
        quickSort(arr, ori_low, high-1)
        quickSort(arr, high+1, pivot_index)
                                    
    
    quickSort(unsorted_list,0,len(unsorted_list)-1)
    return unsorted_list