N = int(input())
numbers = map(int, input().split())

count_zeros = sum(1 for num in numbers if num == 0)

print(count_zeros)
