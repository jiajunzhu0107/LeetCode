
#  There's a quadratic function y = ax2 + bx + c where x is an input and y is the output
#  Given a sorted array as input [x1,x2, x3 .... ] calculate all the output as an array return and return the sorted output array. in a acceding order. 

# a is not 0

# what if b/c is 0

# pivot point, P0 = -b/2a

def quadratic(x, a, b, c):
    return a * x * x + b * x + c

def solution(x, a, b, c): # should be x_array expecially there's another x in another function
    n = len(x) #n is okay, length of array, but better to be array_length
    left = 0 #left_idx
    right = n - 1 #right_idx
    res = [0] * n # res -- resource, output/result
    output_idx = a < 0 ? 
    if a > 0:
        output_idx = n-1 # naming not consistant with left and right
        flag_a = -1 # worst issue, not readable, easy to get trouble
        #another solution is: always output from 0 to n-1, then reverse the output based on a
        # ????, not straight forward, needs to understand the logic of this flag_a before understanding the code
        # compromise of some computation time -- reverse the result -- is better then risk the readability
        ## test case???
        # function -- always focus on the core of this function and straight forward
    else:
        output_idx = 0
        flag_a = 1
# two separate code blocks better not have any couple, otherwise, difficult to understand
#??
    while left <= right:
        # reduction of quadratic calls
        # we already calculated the previous left or right
        # just store it -- TODO
        # naming -- longer is better
        if flag_a * quadratic(x[left], a, b ,c) < flag_a * quadratic(x[right], a, b, c):
            res[output_idx] = quadratic(x[left], a, b ,c)
            left += 1
        else:
            res[output_idx] = quadratic(x[right], a, b ,c)
            right -= 1

        output_idx = output_idx + a < 0 ? -1 : 1
    return res

#not recommending copy paste, lots of bugs genreated by copy pastes

# x = [-3,-2,-1, 0, 1] 
# x = [-3, -2, 0, 1]
# x = [0, 1]
# x = [-1, 0, 1]
x=[] # missing empty
x=[1] # missing single
# expected values
# change a open the prev xs to test again, not required to write assert, expected value first, then test
# not test driven
# why considering pivot?? just considering left - right, balance of left/right
# datatype 
# data range
# consider code path, while, if else
# input different -- empty, single, common validation
# test coverage -- run test cases, how many lines of codes got run
# when it won't be run? if else, loop
# in this case: 2 * 2 * 2 roughly

# 

# readability not good
x = [1, 2, 5]
a = -1
b = 0
c = 0
# -b/2a = 1

res = solution(x, a, b, c)
print(res)
