# /**
# * A tournament tree is a binary tree
# * where the parent is the minimum of the two children.
# * Given a tournament tree find the second minimum value in the tree.
# * A node in the tree will always have 2 or 0 children.
# * Also all leaves will have distinct and unique values.
# *     2             
# *    / \
# *   2   3
# *  / \  | \
# * 4   2 5  3
# *

# * In this given tree the answer is 3.
# */

# class Node {
#   Integer value;
#   Node left, right;
#   Node(Integer value, Node left, Node right) {
#     this.value = value;
#     this.left = left; 
#     this.right = right;
#   }
# }
# class Solution {
#   /**
#   * This should return the second minimum
#   * int value in the given tournament tree
#   */
#   public static Integer secondMin(Node root) {
#     // Fill this up
#   }
# }
from heapq import heappush, heappop
from collections import deque
# def secondMin(Node root):
#     minTwo = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         minTwo.append(node.val)
#         minTwo.sort()
#         if len(minTwo) > 2:
#             minTwo.pop()
#         for child in [node.left, node.right]:
#             if not child:
#                 break
#             queue.append(child)
#     if len(minTwo) == 0:
#         return None
#     elif len(minTwo) == 1:
#         return minTwo[0]
#     return minTwo[1]
def secondMin(Node root):
    res = inf
    def dfs(node):
        if not node.left:
            return
        if node.left.value < node.right.value:
            min_node = node.left
            max_node = node.right
        else:
            min_node = node.right
            max_node = node.left
        res = min(res, max_node.val)
        dfs(min_node)
        
    if not root:
        return None
    if not root.left:
        return root.value
    dfs(root)
    return res


# /* This class will be given a list of words (such as might be tokenized
#  * from a paragraph of text), and will provide a method that takes two
#  * words and returns the shortest distance (in words) between those two
#  * words in the provided text.
#  * Example:
#  *   SentenceDistanceFinder finder = new SentenceDistanceFinder(Arrays.asList("the", "quick", "brown", "fox", "quick"));
#  *   assert(finder.distance("fox", "the") == 3);
#  *   assert(finder.distance("quick", "fox") == 1);
#  *
#  * "quick" appears twice in the input. There are two possible distance values for "quick" and "fox":
#  *     (3 - 1) = 2 and (4 - 3) = 1.
#  * Since we have to return the shortest distance between the two words we return 1.
#  */
# public class SentenceDistanceFinder {
#     public SentenceDistanceFinder(List<String> words) {
#         // implementation here
#     }
#     public int distance(String wordOne, String wordTwo) {
#         // implementation here
#     }
# }

def distance(wordOne, wordTwo):
    lst1 = self.data[wordOne] #sorted list
    lst2 = self.data[wordTwo]
    pointer1 = 0
    pointer2 = 0
    res = inf
    while pointer1 < len(lst1) and pointer2 < len(lst2):
        if lst1[pointer1] == lst2[pointer2]:
            return 0
        elif lst1[pointer1] < lst2[pointer2]:
            res = min(res, lst2[pointer2] - lst1[pointer1])
            pointer1 += 1
        else:
            res = min(res, lst1[pointer1] - lst2[pointer2])
            pointer2 += 1

    return res