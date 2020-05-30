def cal(flag):
    global R, C
    tmp = 0
    if flag:
        switch()
    for j in range(max(R,C)):
        numbers = {}
        for num in board[j]:
            if not num:
                continue
            try:
                numbers[num] += 1
            except KeyError:
                numbers.update({num: 1})
        numbers = [(cnt, num) for num, cnt in numbers.items()]
        numbers.sort()
        i = 0
        board[j] = [0]*100
        for cnt, num in numbers:
            if i == 100:
                break
            board[j][i], board[j][i+1] = num, cnt
            i += 2
        tmp = max(tmp, i)
    if flag:
        R = tmp
        switch()
    else:
        C = tmp


def switch():
    global R, C
    for j in range(max(R,C)):
        for i in range(j, max(R, C)):
            board[j][i], board[i][j] = board[i][j], board[j][i]


r, c, k = map(int, input().split())
board = [[0]*100 for _ in range(100)]
R = C = 3
for j in range(3):
    tmp = list(map(int, input().split()))
    for i in range(3):
        board[j][i] = tmp[i]
ans = 0
while ans <= 100:
    if board[r-1][c-1] == k:
        print(ans)
        break
    ans += 1
    cal(False) if R >= C else cal(True)
else:
    print(-1)