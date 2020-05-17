# Dijkstra Algorithm
import heapq

n = int(input())
m = int(input())

info = {i:{} for i in range(n)}
used = [0] * n
for _ in range(m):
    start, end, cost = map(int, input().split())
    try:
        info[start-1][end-1] = min(info[start-1][end-1], cost)
    except KeyError:
        info[start-1].update({end-1: cost})
start, end = map(int, input().split())
distance = [100000*n] * n
distance[start-1] = 0
Min_heap = []
dist = 0
start, end = start-1, end-1
used[start] = 1
cnt = 0
while cnt < n:
    cnt += 1
    while Min_heap:
        dist, start = heapq.heappop(Min_heap)
        if not used[start]:
            used[start] = 1
            break
    if info.get(start):
        for destination, cost in info[start].items():
            if cost + dist < distance[destination] and not used[destination]:
                heapq.heappush(Min_heap, (cost + dist, destination))
                distance[destination] = cost + dist
print(distance[end])