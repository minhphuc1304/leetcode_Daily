public class Solution {
    public int MaxEvents(int[][] events) {
        Console.WriteLine("abc");
        var ans = 0;

        Array.Sort(events, (a, b) => a[0] - b[0]);
        var lastDay = 0;
        for(var i = 0; i < events.Length; i++) {
            lastDay = Math.Max(lastDay, events[i][1]);
        }

        var heap = new PriorityQueue<int, int>();
        var nextAvailableEventIndex = 0;
        for(var i = 1; i <= lastDay; i++) {
            while(nextAvailableEventIndex < events.Length && events[nextAvailableEventIndex][0] == i) {
                heap.Enqueue(events[nextAvailableEventIndex][1], events[nextAvailableEventIndex][1]);
                nextAvailableEventIndex++;
            }
            
            while(heap.Count > 0 && heap.Peek() < i) {
                heap.Dequeue();
            }

            if(heap.Count > 0) {
                heap.Dequeue();
                ans++;
            }
        }


        return ans;
    }
}
