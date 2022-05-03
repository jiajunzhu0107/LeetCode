# https://leetcode.com/problems/snapshot-array/
# class SnapshotArray:

#     def __init__(self, length: int):
#         self.curr = defaultdict(lambda: 0)
#         self.snap_id = -1
#         self.snapshots = []

#     def set(self, index: int, val: int) -> None:
#         self.curr[index] = val

#     def snap(self) -> int:
#         self.snapshots.append(self.curr.copy())
#         self.snap_id += 1
#         return self.snap_id

#     def get(self, index: int, snap_id: int) -> int:
#         return self.snapshots[snap_id][index]
class SnapshotArray:
    
    def __init__(self, length: int):
        # self.data = {i:[0,{}] for i in range(length)} #{index:{snapId:val}}, -1 for current
        # self.data = {i:0 for i in range(length)}
        self.data = defaultdict(lambda: 0)
        # self.size = length
        # self.snaps = -1
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        # self.data[index][0] = val
        self.data[index] = val

    def snap(self) -> int:
        # self.snaps += 1
        # for i in self.data:
        #     curr_val = self.data[i][0]
        #     if curr_val in self.data[i][1]:
        #         self.data[i][1][curr_val].add(self.snaps)
        #     else:
        #         self.data[i][1][curr_val] = {self.snaps}
            # self.data[i][self.snaps] = self.data[i][-1]
        # self.snaps.append(copy.deepcopy(self.data))
        # return self.snaps
        
        self.snaps.append(self.data.copy())
        # self.snaps.append(copy.deepcopy(self.data))
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        # return self.data[index][snap_id]
        # for val, snapIds in self.data[index][1].items():
        #     if snap_id in snapIds:
        #         return val
        # return 0
        return self.snaps[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)