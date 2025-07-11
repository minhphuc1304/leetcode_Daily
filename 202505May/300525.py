class Solution:
    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)
        

        dist1 = [-1] * n
        current = node1
        d = 0
        while current != -1 and dist1[current] == -1:
            dist1[current] = d
            d += 1
            current = edges[current]
        

        dist2 = [-1] * n
        current = node2
        d = 0
        while current != -1 and dist2[current] == -1:
            dist2[current] = d
            d += 1
            current = edges[current]

        min_max = float('inf')
        answer = -1
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                current_max = max(dist1[i], dist2[i])
                if current_max < min_max:
                    min_max = current_max
                    answer = i
                elif current_max == min_max and i < answer:
                    answer = i
        
        return answer
