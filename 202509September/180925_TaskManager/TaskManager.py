class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.removed_tasks = set()
        self.unique_id_to_task = defaultdict(int)
        self.task_to_unique_id = defaultdict(int)
        self.unique_id_to_version = defaultdict(int)
        self.unique_id_to_user_id = defaultdict(int)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
            
    def add(self, userId: int, taskId: int, priority: int) -> None:
        uniqueId = len(self.unique_id_to_task)
        self.unique_id_to_version[uniqueId] = 0
        self.unique_id_to_user_id[uniqueId] = userId
        self.unique_id_to_task[uniqueId] = taskId
        self.task_to_unique_id[taskId] = uniqueId
        heapq.heappush(self.heap, (-priority, -taskId, userId, 0, uniqueId))

    def edit(self, taskId: int, newPriority: int) -> None:
        uniqueId = self.task_to_unique_id[taskId]
        self.unique_id_to_version[uniqueId] += 1
        heapq.heappush(self.heap, (-newPriority, -taskId, self.unique_id_to_user_id[uniqueId], self.unique_id_to_version[uniqueId], uniqueId))

    def rmv(self, taskId: int) -> None:
        self.removed_tasks.add(self.task_to_unique_id[taskId])
        del self.task_to_unique_id[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, task_id, user_id, version, uniqueId = heapq.heappop(self.heap)
            if uniqueId not in self.removed_tasks and self.unique_id_to_version[uniqueId] == version:
                return user_id
        return -1
        
        
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
