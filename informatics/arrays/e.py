N = int(input())
array = list(map(int, input().split()))

has_same_sign_pair = False

for i in range(1, N):
    if array[i] * array[i - 1] > 0:
        has_same_sign_pair = True
        break

if has_same_sign_pair:
    print("YES")
else:
    print("NO")
