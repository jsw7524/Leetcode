from heapq import heappush, heappop

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append((i + 1, 1))

        result = []
        for query in queries:
            u, v = query
            graph[u].append((v, 1))
            result.append(self.dijkstra(graph, n))

        return result

    def dijkstra(self, graph, n):
        distance = [float('inf')] * n
        distance[0] = 0
        heap = [(0, 0)]

        while heap:
            dist, node = heappop(heap)

            if dist > distance[node]:
                continue

            for neighbor, weight in graph[node]:
                new_distance = distance[node] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heappush(heap, (new_distance, neighbor))

        return distance[n - 1]