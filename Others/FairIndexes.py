# https://algo.monster/problems/fair_indexes
def fairIndexes(A: List[int], B: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if (sum(A) % 2) != 0 or sum(B) != sum(A) or len(A) < 2:
        return 0
    target = sum(A) // 2
    curr_sum = A[0]
    res = 0
    for i in range(1,len(A)):
        
        if curr_sum == target and sum(B[:i]) == target:
            res += 1
        curr_sum += A[i]
    return res