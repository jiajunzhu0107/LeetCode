# https://github.com/python/cpython/blob/d3a8d616faf3364b22fde18dce8c168de9368146/Lib/heapq.py#L263
# https://algo.monster/problems/heap_intro
#not tested
class MinHeap:
	
    def _parrent(self, child_index):
        return (child_index - 1) // 2
    def _left_child(self, parrent_index):
        return 2 * parrent_index + 1
    def _right_child(self, parrent_index):
        return 2 * parrent_index + 2

    def _swapUp(self, heap):
        #curr_node = heap[-1]
        curr_node_index = len(heap) - 1
        parrent_node_index = self._parrent(curr_node_index)
        while heap[parrent_node_index] > heap[curr_node_index] and parrent_node_index >= 0:
            heap[parrent_node_index], heap[curr_node_index] = heap[curr_node_index], heap[parrent_node_index]
            curr_node_index = parrent_node_index
            parrent_node_index = self._parrent(curr_node_index)

    def _swapDown(self, heap):
        #curr_node = heap[-1]
        curr_node_index = 0
		
        while curr_node_index < len(heap)-1:
            left_child_index = self._left_child(curr_node_index)
            right_child_index = self._right_child(curr_node_index)
            if left_child_index < len(heap) and heap[left_child_index] < heap[curr_node_index]:
                heap[left_child_index], heap[curr_node_index] = heap[curr_node_index], heap[left_child_index]
                curr_node_index = left_child_index
            elif right_child_index < len(heap) and heap[right_child_index] < heap[curr_node_index]:
                heap[right_child_index], heap[curr_node_index] = heap[curr_node_index], heap[right_child_index]
                curr_node_index = right_child_index
            else:
                break
			
			
    def push(self, heap, e):
        heap.append(e)
        self._swapUp(heap)

    def pop(self, heap):
        if len(heap) > 0:
            res = heap[0]
            heap[0] = heap.pop()
            self._swapDown(self, heap)
        else:
            res = None # or raise an error
        return res

    def _minHeapify(self, heap, pos):
        while pos < len(heap):
            left_index = self._left_child(pos)
            if left_index >= len(pos):
                return
            right_index = self._right_child(pos)
            if right_index < len(pos) and heap[left_index] > heap[right_index]:
                child_index = right_index
            else:
                child_index = left_index
            if heap[child_index] < heap[pos]:
                heap[pos], heap[child_index] = heap[child_index], heap[pos]
                pos = child_index
                self._minHeapify(heap, pos)
            else:
                return


    def heapify(self, heap):
        for pos in range(len(heap) // 2 - 1, -1, -1):
            self._minHeapify(heap, pos)
	
