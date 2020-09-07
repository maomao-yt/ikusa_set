N = int(input())

ans = []
for i in range(N):
    num = int(input())
    if num % 2 == 1:
        ans.append(num)
ans = sorted(ans)
for answer in ans:
    print(answer)
