from sys import stdin
import heapq
input = stdin.readline

n, m, x = map(int, input().split())
x = x-1
distance = {i: {} for i in range(n)}
for _ in range(m):
    start, end, length = map(int, input().split())
    try:
        distance[start-1][end-1] = min(length, distance[start-1][end-1])
    except KeyError:
        distance[start-1].update({end-1: length})
Min = []
for i in range(n):
    heap = []
    visited = [False] * n
    visited[i] = True
    dist = [101 * 1000]*n
    dist[i] = 0
    start = i
    d0 = 0
    cnt = 0
    while cnt < n:
        cnt += 1
        while heap:
            d0, start = heapq.heappop(heap)
            if not visited[start]:
                visited[start] = True
                break
        if distance.get(start):
            for end, d in distance[start].items():
                if dist[end] > d0 + d:
                    heapq.heappush(heap, (d+d0, end))
                    dist[end] = d0 + d
    Min.append(dist)
ans = 0
for i in range(n):
    ans = max(ans, Min[i][x]+Min[x][i])
print(ans)