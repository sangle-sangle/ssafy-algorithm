from collections import deque


def move(x, d, k):
    global n
    for i in range(n):
        if not (i+1) % x:
            tmp = board[i]
            if d:
                for _ in range(k):
                    tmp.append(tmp.popleft())
            else:
                for _ in range(k):
                    tmp.appendleft(tmp.pop())


def rearrange():
    global n, m
    flag, cnt, Sum = True, 0, 0
    for j in range(n):
        for i in range(m):
            if board[j][i]:
                tmp = board[j][i]
                queue = deque([(i, j)])
                Sum, cnt = Sum + tmp, cnt + 1
                while queue:
                    x0, y0 = queue.popleft()
                    for k in range(4):
                        x, y = x0 + dx[k], y0 + dy[k]
                        if x == -1: x = m-1
                        elif x == m: x = 0
                        if 0 <= y < n and board[y][x] == tmp:
                            board[y0][x0] = board[y][x] = 0
                            queue.append((x, y))
                            flag = False
    if flag and Sum:
        avg = Sum / cnt
        for j in range(n):
            for i in range(m):
                if board[j][i]:
                    if board[j][i] > avg:
                        board[j][i] -= 1
                    elif board[j][i] < avg:
                        board[j][i] += 1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m, t = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int, input().split())
    move(x, d, k)
    rearrange()
ans = 0
for i in range(n):
    ans += sum(board[i])
print(ans)