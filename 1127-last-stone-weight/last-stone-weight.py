class Solution(object):
    def lastStoneWeight(self, stones):
        
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first != second:
                heapq.heappush(max_heap, -(first-second))

        return -max_heap[0] if max_heap else 0           