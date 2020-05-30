def back(init, cnt):
    global n, m, ans
    if cnt == m:
        tmp = 0
        for x, y in house:
            distance = 65
            for x0, y0 in ongoing:
                if distance == 1:
                    break
                distance = min(distance, abs(x-x0)+abs(y-y0))
            tmp += distance
            if tmp >= ans:
                return
        ans = min(tmp, ans)
        return
    for i in range(init, len(chicken)):
        ongoing.append(chicken[i])
        back(i+1, cnt+1)
        ongoing.pop()


n, m = map(int, input().split())
house = []
chicken = []
ongoing = []
ans = 0xfffff
for j in range(n):
    tmp = list(map(int, input().split()))
    for i in range(n):
        if tmp[i] == 1:
            house.append((i, j))
        elif tmp[i] == 2:
            chicken.append((i, j))
back(0, 0)
print(ans)