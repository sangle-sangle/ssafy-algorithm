from heapq import heappush, heappop
def dijkstra(start,s,times):
    heap = []
    times[start] = 0
    heappush(heap,[0,start])
    while heap:
        w, n = heappop(heap)
        if times[n] < w:
            continue
        for to, time in s[n]:
            total = time + w
            if total < times[to]:
                times[to] = total
                heappush(heap, [total, to])

N, M, X = map(int,input().split())
roads = [list(map(int,input().split())) for _ in range(M)]

s = [[] for i in range(N)]
r = [[] for i in range(N)]
times = [0xffff] * N
rtimes = [0xffff] * N
for road in roads:
    a,b,t = road
    s[a-1].append([b-1,t])
    r[b-1].append([a-1,t])

dijkstra(X-1,s,times)
dijkstra(X-1,r,rtimes)
print(times)
print(rtimes)
result = 0
for i in range(N):
    result = max(result,times[i]+rtimes[i])
print(result)