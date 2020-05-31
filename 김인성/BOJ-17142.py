from collections import deque


def back(init, cnt):
    global n, m, wall, ans
    if cnt == m:
        visited = [[False] * n for _ in range(n)]
        queue = deque()
        for x, y in start:
            queue.append((x, y))
            visited[y][x] = True
        vacant = n**2 - wall
        time = 0
        while queue and vacant:
            time += 1
            if time >= ans: return
            for _ in range(len(queue)):
                x0, y0 = queue.popleft()
                for i in range(4):
                    x, y = x0 + dx[i], y0 + dy[i]
                    if 0 <= x < n and 0 <= y < n and not visited[y][x] and board[y][x] != 1:
                        visited[y][x] = True
                        queue.append((x, y))
                        if not board[y][x]: vacant -= 1
        if not vacant:
            ans = min(ans, time)
        return
    for i in range(init, len(origin)):
        if len(origin) - i < m - cnt:
            return
        start.append(origin[i])
        back(i+1, cnt+1)
        start.pop()


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = []
origin = []
wall = 0
ans = n**2
for j in range(n):
    tmp = list(map(int, input().split()))
    for i in range(n):
        if tmp[i] == 2:
            origin.append((i, j))
            wall += 1
        elif tmp[i] == 1:
            wall += 1
    board.append(tmp)
start = []
back(0, 0)
if ans == n**2: ans = -1
print(ans)