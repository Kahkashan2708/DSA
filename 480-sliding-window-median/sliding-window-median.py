import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):
        maxHeap = []  # smaller half (as negative values)
        minHeap = []  # larger half
        delayed = defaultdict(int)  # lazy delete map
        maxSize = minSize = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap is maxHeap else heap[0]
                if delayed[num]:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal maxSize, minSize
            # maxHeap should always have >= size than minHeap
            if maxSize > minSize + 1:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
                maxSize -= 1
                minSize += 1
                prune(maxHeap)
            elif maxSize < minSize:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                maxSize += 1
                minSize -= 1
                prune(minHeap)

        def add(num):
            nonlocal maxSize, minSize
            if not maxHeap or num <= -maxHeap[0]:
                heapq.heappush(maxHeap, -num)
                maxSize += 1
            else:
                heapq.heappush(minHeap, num)
                minSize += 1
            balance()

        def remove(num):
            nonlocal maxSize, minSize
            delayed[num] += 1
            if num <= -maxHeap[0]:
                maxSize -= 1
                if num == -maxHeap[0]:
                    prune(maxHeap)
            else:
                minSize -= 1
                if minHeap and num == minHeap[0]:
                    prune(minHeap)
            balance()

        def getMedian():
            if k % 2:
                return float(-maxHeap[0])
            return (-maxHeap[0] + minHeap[0]) / 2

        result = []
        for i in range(len(nums)):
            add(nums[i])
            if i >= k:
                remove(nums[i - k])
            if i >= k - 1:
                result.append(getMedian())

        return result


        