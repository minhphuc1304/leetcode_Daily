from typing import List
from heapq import heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()

        # Min-heaps for available rooms and busy rooms
        available = list(range(n)) # room indices
        busy = [] # (end_time, room_index)

        # Count of how many times each room is used 
        count = [0] * n

        for start, end in meetings:
            # Free up rooms whose meetings have ended
            while busy and busy[0][0] <= start:
                end_time, room = heappop(busy)
                heappush(available, room)

            if available:
                # Assign the meeting to the available room with the smallest index
                room = heappop(available)
                heappush(busy, (end, room))
                count[room] += 1
            else:
                # All rooms are busy, wait for the earliest one to be free
                end_time, room = heappop(busy)
                duration = end - start
                new_end = end_time + duration
                heappush(busy, (new_end, room))
                count[room] += 1

        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return i
        
        return 0


test_cases = [
    {
        "n": 2,
        "meetings": [[0, 10], [1, 5], [2, 7], [3, 4]],
        "expected": 0
    },
    {
        "n": 3,
        "meetings": [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]],
        "expected": 1
    }
]

if __name__ == "__main__":
    sol = Solution()
