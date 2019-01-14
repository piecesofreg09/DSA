# python3
import heapq

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        
        self.available_workers = list(range(self.num_workers))
        heapq.heapify(self.available_workers)
        self.working_workers = []
        heapq.heapify(self.working_workers)

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        cur = 0

        for i in range(len(self.jobs)):
            if len(self.available_workers) == 0:
                time_finished, worker_vacant = heapq.heappop(self.working_workers)
                cur = time_finished
                heapq.heappush(self.available_workers, worker_vacant)
            worker = heapq.heappop(self.available_workers)
            self.start_times[i] = cur
            self.assigned_workers[i] = worker
            heapq.heappush(self.working_workers, (self.jobs[i] + cur, worker))

        
        
        '''
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
        '''

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

