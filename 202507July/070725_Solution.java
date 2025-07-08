class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> a[0] - b[0]);

        int lastDay = 0;
        for (int[] event: events) {
            lastDay = Math.max(lastDay, event[1]);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int count = 0;
        int i = 0;
        for (int d = 1; d <= lastDay; ++d) {
            while (!pq.isEmpty() && pq.peek() < d) {
                pq.poll();
            }

            while (i < events.length && events[i][0] <= d) {
                pq.add(events[i][1]);
                i++;
            }

            if (!pq.isEmpty()) {
                pq.poll();
                count++;
            }
        }

        return count;
    }
}
