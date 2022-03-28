# https://algo.monster/problems/partition_array_into_n_subsets_with_balanced_sum
# is it certain the result will be the minimum absolute difference?

def partition(arr: List[int], N: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    heap = [(0,i) for i in range(N)]
    res = [[] for i in range(N)]
    for a in sorted(arr,reverse = True):
        val,ind = heappop(heap)
        total = val + a
        heappush(heap,(total,ind))
        res[ind].append(a)
    return res