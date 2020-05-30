n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0xffff
for y0 in range(n-2):
    for x0 in range(1, n-1):
        for k1 in range(x0, 0, -1):
            for k2 in range(n-x0-1, 0, -1):
                if not ans:
                    break
                if k1 + k2 + y0 < n:
                    x1, y1 = x0 + k2 - k1, k1 + k2 + y0
                    y2, y3 = y0 + k1, y0 + k2
                    city = [0, 0, 0, 0, 0]
                    for y in range(n):
                        for x in range(n):
                            if x + y < x0 + y0 and x <= x0 and y < y2:
                                city[0] += board[y][x]
                            elif x - y > x0 - y0 and x > x0 and y <= y3:
                                city[1] += board[y][x]
                            elif x - y < x1 - y1 and x < x1 and y >= y2:
                                city[2] += board[y][x]
                            elif x + y > x1 + y1 and x >= x1 and y > y3:
                                city[3] += board[y][x]
                            else:
                                city[4] += board[y][x]
                    ans = min(ans, max(city) - min(city))
print(ans)