class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap=[]
        self.dic={}
        for i,j,k in tasks:
            heapq.heappush(self.heap,(-k,-j,i))
            self.dic[j]=(k,i)            

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap,(-priority,-taskId,userId))
        self.dic[taskId]=(priority,userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        p,uid=self.dic[taskId]
        self.dic[taskId]=(newPriority,uid)
        heapq.heappush(self.heap,(-newPriority,-taskId,uid))

    def rmv(self, taskId: int) -> None:
        del self.dic[taskId] 

    def execTop(self) -> int:
        while self.heap:
            p1,tid,uid1=heapq.heappop(self.heap)
            tid=-tid
            if tid in self.dic:
                p2,uid2=self.dic[tid]
                if -p1==p2 and uid1==uid2:
                    del self.dic[tid]
                    return uid1
        return -1

        
        



        





# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()