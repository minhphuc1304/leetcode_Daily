from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        size = len(startTime)
        gapsArr, left = [], 0
        for i in range(size):
            gap = startTime[i] - left
            gapsArr.append(gap)
            left = endTime[i]
        
        gapsArr.append(eventTime - endTime[-1])
        maxGapPrefix, maxGapSuffix = [0 for i in range(size)], [0 for i in range(size)]
        maxGapPrefix[0] = gapsArr[0]
        maxGapSuffix[size - 1] = gapsArr[-1]

        for i in range(1, size):
            maxGapPrefix[i] = max(maxGapPrefix[i - 1], gapsArr[i])
        for i in range(size - 1, 0, -1):
            maxGapSuffix[i - 1] = max(maxGapSuffix[i], gapsArr[i])

        ans = 0
        for i in range(size):
            curr = gapsArr[i] + gapsArr[i + 1]
            barSize = endTime[i] - startTime[i]
            isValid = False
            if (i - 1 >= 0):
                isValid = isValid or maxGapPrefix[i - 1] >= barSize
            if (i + 1 < size):
                isValid = isValid or maxGapSuffix[i + 1] >= barSize
            if (isValid):
                curr += barSize 
            ans = max(ans, curr)

        return ans


# if __name__ == "__main__":
#     sol = Solution()

#     eventTime = 20
#     startTime = [2, 8, 14]
#     endTime = [6, 10, 18]

#     result = sol.maxFreeTime(eventTime, startTime, endTime)
#     print("Max continous free time: ", result)

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "eventTime": 20,
            "startTime": [2, 8, 14],
            "endTime": [6, 10, 18],
            "expected": 8
        },
        {
            "eventTime": 5,
            "startTime": [1, 3],
            "endTime": [2, 5],
            "expected": 2
        },
        {
            "eventTime": 10,
            "startTime": [0, 7, 9],
            "endTime": [1, 8, 10],
            "expected": 7
        },
        {
            "eventTime": 10,
            "startTime": [0, 3, 7, 9],
            "endTime": [1, 4, 8, 10],
            "expected": 6
        },
        {
            "eventTime": 5,
            "startTime": [0, 1, 2, 3, 4],
            "endTime": [1, 2, 3, 4, 5],
            "expected": 0
        }
    ]

    for idx, test in enumerate(test_cases):
        result = sol.maxFreeTime(test["eventTime"], test["startTime"], test["endTime"])
        status = "PASS" if result == test["expected"] else f"FAIL (got {result})"
        print(f"Test case #{idx + 1}: {status}")