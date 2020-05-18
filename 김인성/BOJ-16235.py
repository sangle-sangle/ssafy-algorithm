import heapq
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
n, m, k = map(int, input().split())
land = [[5]*n for _ in range(n)]
fertilizer = [list(map(int, input().split())) for _ in range(n)]
tree = {}
for _ in range(m):
    y, x, z = map(int, input().split())
    tree.update({(x-1, y-1): [z]})
for _ in range(k):
    if not m:
        break
    new_tree = {}
    for j in range(n):
        for i in range(n):
            if tree.get((i, j)):
                trees = tree.pop((i, j))
                while trees:
                    # spring
                    if trees[0] <= land[j][i]:
                        age = heapq.heappop(trees)
                        land[j][i] -= age
                        # fall
                        if not (age + 1) % 5:
                            for k in range(8):
                                x, y = i + dx[k], j + dy[k]
                                if 0 <= x < n and 0 <= y < n:
                                    m += 1
                                    if new_tree.get((x, y)):
                                        heapq.heappush(new_tree[(x, y)], 1)
                                    else:
                                        new_tree.update({(x, y): [1]})
                        if new_tree.get((i, j)):
                            heapq.heappush(new_tree[(i, j)], age+1)
                        else:
                            new_tree.update({(i, j): [age+1]})
                    # summer
                    else:
                        for _ in range(len(trees)):
                            m -= 1
                            land[j][i] += (trees.pop() // 2)
            # winter
            land[j][i] += fertilizer[j][i]
    tree, new_tree = new_tree, {}
print(m)