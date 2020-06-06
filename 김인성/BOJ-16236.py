from collections import deque
import heapq


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())
board = []
fishes = [0]*7
size, time, eat = 2, 0, 2
for j in range(n):
    tmp = list(map(int, input().split()))
    for i in range(n):
        if tmp[i] == 9:
            baby, tmp[i] = (i, j), 0
        elif tmp[i]:
            fishes[tmp[i]] += 1
    board.append(tmp)
queue = deque([baby])
while sum(fishes[:size]):
    heap = []
    tmp_time = 0
    visited = [[False]*n for _ in range(n)]
    visited[baby[1]][baby[0]] = True
    while queue or heap:
        if heap:
            baby = heapq.heappop(heap)
            baby = (baby[1], baby[0])
            queue = deque([baby])
            fishes[board[baby[1]][baby[0]]] -= 1
            board[baby[1]][baby[0]] = 0
            time += tmp_time
            eat -= 1
            if not eat:
                size, eat = size+1, size+1
            break
        tmp_time += 1
        for _ in range(len(queue)):
            x0, y0 = queue.popleft()
            for i in range(4):
                x, y = x0 + dx[i], y0 + dy[i]
                if 0 <= x < n and 0 <= y < n and not visited[y][x]:
                    if board[y][x] == size or not board[y][x]:
                        queue.append((x, y))
                        visited[y][x] = True
                    elif 0 < board[y][x] < size:
                        heapq.heappush(heap, (y, x))
                        visited[y][x] = True
    else:
        break
print(time)