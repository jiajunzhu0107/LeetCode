tiles game: thera re 9 tiles in a deck, each tile has unique numbrer of from [1, 9]

there will be 4 decks in total, 4 * 9 = 36 tiles in total,

write a program to decide if a hand is a winning hand (a random draw of 12 tiles).

a winning hand: there are 4 patterns, with each tile is used exactly once
pattern: 3 consecutive numbers, or 3 numbers of the same


winning hand example: [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]

not a winning hand: [1, 2, 3,] 5, 6, 6, 8, 8, 8, [3, 3, 3]

# 1, 1, 1, 1
# [], len == 12
# output True -- win, False -- lose

# 1,1,1, 222, 333
# 1, 2, 3 ,3, 3,4,5,4,5, 9,9,9, 3 + 2 = 5 > 4
# 

[1, 1, 1], [2, 2, 2], [3, 3, 3], 4, 4, 5
#123,123,123/345
# 111,222, 333
#[1,2,3], []


another hand: 555, 666, 777, 348

[]
root [1]
1,1,1, 2
1,2,

[1,1,1], [2], [1,2,3]


111 222 333 444


left 3 same, right cons
dic {1:0, 2:3, 3:3, 4:}
1
1, (2)
1,2
2,
2,
2
