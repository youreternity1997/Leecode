# Time complexity: O(V+E)O(V + E)O(V+E)
# Space complexity: O(V+E)O(V + E)O(V+E)

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        prerequisites_count = [0] * n
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            prerequisites_count[course] += 1
            #print('adj=', adj)
            #print('prerequisites_count=', prerequisites_count)

        queue = deque()
        for i in range(n):
            if prerequisites_count[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                prerequisites_count[next_course] -= 1
                if prerequisites_count[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == n