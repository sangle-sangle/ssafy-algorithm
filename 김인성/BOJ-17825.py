def back(cnt, mals, result):
    if cnt == 10:
        global answer
        if answer < result:
            answer = result
        return
    for i in range(4):
        pos = [mals[i][0], mals[i][1]]
        if pos[0] == 5:
            continue
        next_pos = [pos[0], pos[1] + dice[cnt]]
        if next_pos[1] > length[next_pos[0]]:
            if next_pos[0] == 0 or next_pos[0] == 4:
                mals[i] = [5, 0]
            else:
                if next_pos[1] - length[next_pos[0]] > 4:
                    mals[i] = [5, 0]
                else:
                    mals[i] = [4, next_pos[1] - length[pos[0]] - 1]
        elif next_pos[0] == 0:
            if next_pos[1] == 5:
                mals[i] = [1, 0]
            elif next_pos[1] == 10:
                mals[i] = [2, 0]
            elif next_pos[1] == 15:
                mals[i] = [3, 0]
            else:
                mals[i][1] = next_pos[1]
        else:
            mals[i][1] = next_pos[1]

        if mals[i][0] == 4 and mals[i][1] == 3:
            mals[i] = [0, 20]
        if mals[i][0] == 5:
            pass
        else:
            flag = False
            for j in range(4):
                if i == j:
                    continue
                if mals[j] == mals[i]:
                    mals[i] = pos
                    flag = True
                    break
            if flag:
                continue
        if mals[i][0] != 5:
            tmp = board[mals[i][0]][mals[i][1]]
        else:
            tmp = 0
        back(cnt + 1, mals, result + tmp)
        mals[i] = pos


board = [
    [2*i for i in range(21)],
    [10, 13, 16, 19],
    [20, 22, 24],
    [30, 28, 27, 26],
    [25, 30, 35, 40],
]
length = [20, 3, 2, 3, 3]
mals = [[0, 0] for _ in range(4)]
dice = list(map(int, input().split()))
answer = 0
back(0, mals, 0)
print(answer)