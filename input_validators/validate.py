import sys
n = int(input())
if n < 1 or n > 400:
    sys.exit(1)
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        sys.exit(1)
    for elem in row:
        if elem != 0 and elem != 1:
            sys.exit(1)
## now if there is any more input to get
try:
    input()
    print("extra input")
    sys.exit(1)
except EOFError:
    pass
#print("ok")
sys.exit(42)