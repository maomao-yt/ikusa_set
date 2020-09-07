N = int(input())

answer = []
for i in range(N):
    name = input()
    answer.append(name)
    if answer.count(name) > 1:
        print("NO")
    else:
        print("YES")
