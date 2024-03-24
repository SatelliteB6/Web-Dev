N = int(input())
array = list(map(int, input().split()))

for i in range(N // 2):
    array[i], array[N - 1 - i] = array[N - 1 - i], array[i]

print(*array)
