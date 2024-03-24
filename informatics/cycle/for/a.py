a = int(input())
b = int(input())

result = ""

for num in range(a, b + 1):
    if num % 2 == 0:
        result += str(num) + " "

print(result.rstrip())
