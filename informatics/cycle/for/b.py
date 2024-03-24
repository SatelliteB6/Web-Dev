a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = ""

for num in range(a, b + 1):
    if num % d == c:
        result += str(num) + " "

print(result.rstrip())
