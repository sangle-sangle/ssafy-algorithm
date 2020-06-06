import heapq

def move(x0, y0, s, d0):
    global r, c
    x, y = x0 + s*dx[d0], y0 + s*dy[d0]
    if d0 > 1:
        xq, xr = x // (c - 1), x % (c - 1)
        if xq % 2:
            return c- 1 - xr, y, 5 - d0
        else:
            return xr, y, d0
    else:
        yq, yr = y // (r - 1), y % (r - 1)
        if yq % 2:
            return x, r - 1 - yr, 1 - d0
        else:
            return x, yr, d0


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
r, c, m = map(int, input().split())
sharks = {}
heap = []
for _ in range(m):
    y, x, s, d, z = map(int, input().split())
    sharks.update({(x-1, y-1): (s, d-1, z)})
    if not x-1:
        heapq.heappush(heap, y-1)
time = 0
ans = 0
while c - time > 0:
    new_sharks = {}
    if heap:
        y = heapq.heappop(heap)
        s, d, z = sharks.pop((time, y))
        ans += z
    heap = []
    time += 1
    for (x0, y0), (s, d0, z) in sharks.items():
        x, y, d = move(x0, y0, s, d0)
        if x == time:
            heapq.heappush(heap, y)
        if new_sharks.get((x, y)):
            if new_sharks[(x, y)][2] < z:
                new_sharks[(x, y)] = (s, d, z)
        else:
            new_sharks.update({(x, y): (s, d, z)})
    sharks = new_sharks
print(ans)