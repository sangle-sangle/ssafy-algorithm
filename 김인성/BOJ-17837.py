dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
drones = {}
position = []
for idx in range(k):
    y, x, d = map(int, input().split())
    drones.update({(x-1, y-1): [idx]})
    position.append((x-1, y-1, d-1))
time = 0
flag = True
while flag and time < 1000:
    time += 1
    for i in range(k):
        x0, y0, d0 = position[i]
        drone_set = drones[(x0, y0)]
        j = drone_set.index(i)
        drones[(x0, y0)], tmp = drone_set[:j], drone_set[j:]
        if not drones[(x0, y0)]:
            drones.pop((x0, y0))
        x, y, d = x0 + dx[d0], y0 + dy[d0], d0
        if not (0 <= x < n and 0 <= y < n and board[y][x] != 2):
            d = d0 - 1 if d0 % 2 else d0 + 1
            x, y = x0 + dx[d], y0 + dy[d]
            if not (0 <= x < n and 0 <= y < n and board[y][x] != 2):
                x, y = x0, y0
            else:
                if board[y][x] ==    1:
                    tmp.reverse()
        else:
            if board[y][x] == 1:
                tmp.reverse()
        position[i] = (x, y, d)
        for idx in tmp:
            position[idx] = (x, y, position[idx][2])
        next_position = drones.get((x, y))
        if next_position:
            next_position.extend(tmp)
        else:
            drones.update({(x, y): tmp})
        if len(drones[(x, y)]) >= 4:
            flag = False
            print(time)
            break
if flag:
    print(-1)