N = int(input())

for i in range(N):
    word = input()
    if word == "forward":
        print("Sunny")
    elif word == "reverse":
        print("Rainy")
    else:
        print("Cloudy")
