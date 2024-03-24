N = int(input())
array = list(map(int, input().split()))

count_special = 0

for i in range(1, N - 1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count_special += 1

print(count_special)
