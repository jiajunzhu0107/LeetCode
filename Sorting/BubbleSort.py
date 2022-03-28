# https://algo.monster/problems/sorting_intro

def sort_list(unsorted_list: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(unsorted_list)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True
        if not swapped:
            return unsorted_list
    return unsorted_list