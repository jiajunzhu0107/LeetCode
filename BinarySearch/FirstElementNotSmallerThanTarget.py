# https://algo.monster/problems/binary_search_first_element_not_smaller_than_target

def first_not_smaller(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)
    left = 0
    right = n - 1
    possible_boundary = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            possible_boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return possible_boundary