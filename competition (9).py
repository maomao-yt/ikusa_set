N, M = map(int, input().split())

field = []
# 2次元リストマップを作成
for i in range(N):
    sub_field = []
    lines = input()
    for dot in lines:
        sub_field.append(dot)
    field.append(sub_field)

num = 0

for y in range(N):
    for x in range(M):
        if field[y][x] == "#":
            num += 1

yoko = 0
tate = 0
ten = 0
for y in range(N):
    for x in range(M):
        # 線対称ならば(横)
        if field[y][x] == "#" and field[y][M - x - 1] == "#":
            yoko += 1
        # 線対称ならば(縦)
        if field[y][x] == "#" and field[N - y - 1][x] == "#":
            tate += 1
        # 点対称ならば
        if field[y][x] == "#" and field[N - y - 1][M - x - 1] == "#":
            ten += 1

if yoko == num or tate == num:
    if ten == num:
        print("line point symmetry")
    else:
        print("line symmetry")
elif ten == num:
    print("point symmetry")
else:
    print("none")
