# https://algo.monster/problems/sorting_intro


def sort_list(unsorted_list: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(unsorted_list)
    for i in range(n):
        ind_min = i
        for j in range(i,n):
            if unsorted_list[j] < unsorted_list[ind_min]:
                ind_min = j
        unsorted_list[i], unsorted_list[ind_min] = unsorted_list[ind_min], unsorted_list[i]
    return unsorted_list